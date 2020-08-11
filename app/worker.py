import time
from datetime import datetime, timedelta

from PySide2.QtCore import QEventLoop

from app.connectors.connector_1c import Connector1c
from app.connectors.connector_csv import ConnectorCSV
from app.connectors.connector_excel import ConnectorExcel
from app.shared.api_service import ApiService
from app.shared.constants import Constants
from app.shared.helpers import obj, Helpers
from app.shared.storage_service import StorageService
from app.shared.text_logger import TextLogger


class Worker(obj):
    is_connected = False
    connector = None

    def __init__(self, parent, company):
        super(Worker, self).__init__()
        self.parent = parent
        self.company = company
        self.logging = TextLogger(company=self.company).log
        self.init_connector()

    def init_connector(self):
        self.disconnect()

        if self.company.int_source_type == 0:  # 1c
            self.connector = Connector1c(self, self.company)
        elif self.company.int_source_type == 1:  # excel
            self.connector = ConnectorExcel(self, self.company)
        elif self.company.int_source_type == 2:  # csv
            self.connector = ConnectorCSV(self, self.company)

    def connect(self):
        try:
            self.init_connector()
            if self.connector is None:
                raise Exception('Коннектор не определен')
            self.log('Соединяюсь с источником...')
            result = self.connector.connect()
            self.is_connected = result is not None and result != False
        except Exception as e:
            self.log(e, True)
            self.is_connected = False
        return self.is_connected

    def disconnect(self):
        if self.connector is not None:
            self.connector.disconnect()

    def check_connection(self):
        self.is_connected = self.connector is not None and self.connector.is_connected()
        if self.is_connected:
            return True

        attempts = 1
        while attempts < 4:
            self.log('Попытка соединения # {}'.format(str(attempts)))
            if self.connect():
                return True
            else:
                attempts += 1
                time.sleep(3)

        return False

    def log(self, text, is_error=False, is_success=False, is_warning=False):
        if self.company:
            text = "[ {} ] {}".format(self.company.ext_name, text)
        if is_error:
            self.logging.error(text)
        elif is_warning:
            self.logging.warning(text)
        elif is_success:
            self.logging.log(Constants.LOG_GOOD, text)
        else:
            self.logging.info(text)

    def find_company_in_source(self, on_success=lambda x: x, on_error=lambda x: x):
        if not self.check_connection():
            return on_error('Нет связи с источником данных, отмена')

        try:
            company_from_source = self.connector.get_company()
        except Exception as err:
            self.log(err)
            on_error(err)
            return

        # setting new values from source
        if company_from_source:
            self.company.int_inn = company_from_source.int_inn
            self.company.int_name = company_from_source.int_name
            on_success(company_from_source)
        else:
            err = 'Компания с ИНН {} не найдена в источнике'.format(self.company.ext_inn)
            self.log(err)
            on_error(err)

        return

    def sync_items_from_server(self, on_success=lambda x: x, on_error=lambda x: x):
        self.update_company({
            'sync_server_items_now': True
        })
        
        last_update = self.company.sync_server_items

        if last_update:
            self.log('Обновляю товары с сервера Tarder с момента последнего обновления ({})'
                     .format(Helpers.get_pretty_date(last_update)))
        else:
            self.log('Получаю все товары с сервера Tarder')

        def on_success_int(result):
            if result.items is not None:
                items = result.items
                count_items = len(items)
                self.log('Получено товаров: ' + str(count_items), is_success=True)

                if count_items > 0:
                    StorageService().upsert_items(items, on_success, on_error)
                else:
                    on_success(True)

                self.update_company({
                    'sync_server_items_now': False,
                    'sync_server_items': result.date and str(result.date) or str(Helpers.now()),
                })

            else:
                err = 'Ошибка получения данных: пустой ответ от сервера'
                self.log(err, True)
                on_error(err)
                self.update_company({
                    'sync_server_items_now': False,
                    'sync_server_items_error': str(Helpers.now()),
                })
            pass

        def on_error_int(error):
            self.log('Ошибка получения данных: ' + str(error), True)
            on_error(error)
            self.update_company({
                'sync_server_items_now': False,
                'sync_server_items_error': str(Helpers.now()),
            })
            pass

        self.update_company({
            'sync_server_items_now': True,
        })

        query = {
            'companyId': self.company.ext_id
        }

        if last_update:
            query['lastUpdate'] = last_update

        ApiService().get_items(query, on_success_int, on_error_int)

    def sync_items_from_source(self, on_success=lambda x: x, on_error=lambda x: x):
        if not self.check_connection():
            return on_error('Нет связи с источником данных, отмена')
        
        self.update_company({
            'sync_source_items_now': True
        })

        self.log('Сопоставляю товары из источника с товарами в Tarder')

        try:
            array_from_base = StorageService().get_items(self.company.ext_id, exist_ext_id_internal=True)
            if len(array_from_base) == 0:
                raise Exception('У компании нет загруженных с сервера товаров')

            array_from_source = self.connector.get_items(list(map(lambda x: x.ext_id_internal, array_from_base)))

            # for case - if not found in base - set null
            StorageService().clear_items_source(self.company.ext_id)
        except Exception as error:
            self.log('Ошибка обновления товаров из источника: ' + str(error), True)
            self.update_company({
                'sync_source_items_now': False,
                'sync_source_items_error': str(Helpers.now()),
            })
            on_error(error)
            return


        def on_success_int(result):
            self.update_company({
                'sync_source_items_now': False,
                'sync_source_items': str(Helpers.now()),
            })
            on_success(True)
            
        def on_error_int(error):
            self.log('Ошибка обновления товаров из источника: ' + str(error), True)
            self.update_company({
                'sync_source_items_now': False,
                'sync_source_items_error': str(Helpers.now()),
            })
            on_error(error)

        # setting new values from source
        StorageService().update_items_from_source(self.company.ext_id, array_from_source, on_success_int, on_error_int)
        return

    def sync_points_from_server(self, on_success=lambda x: x, on_error=lambda x: x):
        self.update_company({
            'sync_server_points_now': True
        })
        
        last_update = self.company.sync_server_points

        if last_update:
            self.log('Обновляю точки продаж с сервера Tarder с момента последнего обновления ({})'
                     .format(Helpers.get_pretty_date(last_update)))
        else:
            self.log('Получаю все точки продаж с сервера Tarder')

        def on_success_int(result):
            if result.items is not None:
                items = result.items
                count_items = len(items)
                self.log('Получено точек продаж: ' + str(count_items), is_success=True)

                if count_items > 0:
                    StorageService().upsert_points(items, on_success, on_error)
                else:
                    on_success(True) 
                
                self.update_company({
                    'sync_server_points_now': False,
                    'sync_server_points': result.date and str(result.date) or str(Helpers.now()),
                })

            else:
                err = 'Ошибка получения данных: пустой ответ от сервера'
                self.log(err, True)
                on_error(err)
                self.update_company({
                    'sync_server_points_now': False,
                    'sync_server_points_error': str(Helpers.now()),
                })
            pass

        def on_error_int(error):
            self.log('Ошибка получения данных: ' + str(error), True)
            on_error(error)
            self.update_company({
                'sync_server_points_now': False,
                'sync_server_points_error': str(Helpers.now()),
            })
            pass

        query = {
            'companyId': self.company.ext_id
        }

        if last_update:
            query['lastUpdate'] = last_update

        ApiService().get_points(query, on_success_int, on_error_int)

    def sync_points_from_source(self, on_success=lambda x: x, on_error=lambda x: x):
        if not self.check_connection():
            return on_error('Нет связи с источником данных, отмена')
        
        self.update_company({
            'sync_source_points_now': True
        })

        self.log('Сопоставляю склады из источника с точками продаж в Tarder')

        try:
            array_from_base = StorageService().get_points(self.company.ext_id, exist_ext_id_internal=True)
            if len(array_from_base) == 0:
                raise Exception('У компании нет загруженных с сервера точек продаж')
            array_from_source = self.connector.get_points(list(map(lambda x: x.ext_id_internal, array_from_base)))
        except Exception as error:
            self.log(str(error), True)
            self.update_company({
                'sync_source_points_now': False,
                'sync_source_points_error': str(Helpers.now()),
            })
            on_error(error)
            return

        def on_success_int(result):
            self.update_company({
                'sync_source_points_now': False,
                'sync_source_points': str(Helpers.now()),
            })
            on_success(True)
            
        def on_error_int(error):
            self.log(str(error), True)
            on_error(error)
            self.update_company({
                'sync_source_points_now': False,
                'sync_source_points_error': str(Helpers.now()),
            })

        # setting new values from source
        StorageService().update_points(array_from_source, on_success_int, on_error_int)

    def get_types_of_price(self, on_success=lambda x: x, on_error=lambda x: x):
        if not self.check_connection():
            return on_error('Нет связи с источником данных, отмена')

        try:
            type_of_prices = self.connector.get_types_of_prices()
        except Exception as e:
            return on_error(e)

        return on_success(type_of_prices)

    def sync_iip_from_source(self, on_success=lambda x: x, on_error=lambda x: x):
        if not self.check_connection():
            return on_error('Нет связи с источником данных, отмена')
        
        self.update_company({
            'sync_source_iip_now': True
        })

        self.log('Получаю остатки и цены из источника')
        
        try:
            points_from_base = StorageService().get_points(self.company.ext_id, exist_ext_id_internal=True)
            items_from_base = StorageService().get_items(self.company.ext_id, exist_ext_id_internal=True)
            if len(items_from_base) == 0:
                raise Exception('Нет товаров')
            if len(points_from_base) == 0:
                raise Exception('Нет точек продаж')

            if self.company.int_type_price is None and self.connector.is_type_price_required:
                self.log('Тип цен не выбран, хотя он является обязательным для этого типа соединения, '
                         'будут загружены только остатки', is_warning=True)

            array_from_source = self.connector.get_count_and_price_in_points(
                list(map(lambda x: x.ext_id_internal, items_from_base)),
                list(map(lambda x: x.ext_id_internal, points_from_base)),
                self.company.int_type_price
            )
        except Exception as error:
            self.log('Ошибка обновления товаров из источника: ' + str(error), True)
            self.update_company({
                'sync_source_iip_now': False,
                'sync_source_iip_error': str(Helpers.now()),
            })
            on_error(error)
            return

        def on_success_int(result):
            self.update_company({
                'sync_source_iip_now': False,
                'sync_source_iip': str(Helpers.now()),
            })
            on_success(True)

        def on_error_int(error):
            self.log('Ошибка обновления товаров из источника: ' + str(error), True)
            self.update_company({
                'sync_source_iip_now': False,
                'sync_source_iip_error': str(Helpers.now()),
            })
            on_error(error)

        array_missing_iip = []

        # add empty value for missing items or points
        for item in items_from_base:
            for point in points_from_base:
                item_from_source = next(filter(lambda x:
                                               x.item_id_internal == item.ext_id_internal and
                                               x.point_id_internal == point.ext_id_internal, array_from_source), None)
                if not item_from_source:
                    item_new = obj()
                    item_new.item_id_internal = item.ext_id_internal
                    item_new.point_id_internal = point.ext_id_internal

                    item_new.int_price = None
                    item_new.int_count = None
                    array_missing_iip.append(item_new)

        array_from_source += array_missing_iip
        # setting new values from source
        StorageService().upsert_iip(array_from_source, on_success_int, on_error_int)
        return

    def upload_iip_to_server(self, on_success=lambda x: x, on_error=lambda x: x):
        
        self.update_company({
            'sync_server_iip_now': True
        })

        self.log('Выгружаю остатки и цены на сервер Tarder')

        def on_success_int(result):
            if result:
                self.log('Получено обновленных остатков и цен в точках продаж: ' + str(len(result)), is_success=True)

                array = []

                for item_from_server in result:
                    item_exist = next(filter(lambda x:
                                             x.itemId == item_from_server.itemId
                                             and x.pointOfSaleId == item_from_server.pointOfSaleId, items_raw), None)
                    if not item_exist:
                        self.log('Не найден елемент для сохранения ответа с свервера', True)
                    else:
                        item_to_update = obj()
                        item_to_update.ext_id = item_from_server.id
                        item_to_update.ext_count = item_from_server.count
                        item_to_update.ext_price = item_from_server.price

                        item_to_update.item_id_internal = item_exist.item_id_internal
                        item_to_update.point_id_internal = item_exist.point_id_internal
                        array.append(item_to_update)

                def on_success_int2(result):
                    self.update_company({
                        'sync_server_iip_now': False,
                        'sync_server_iip': str(Helpers.now()),
                    })
                    on_success(result)

                def on_error_int2(error):
                    self.update_company({
                        'sync_server_iip_now': False,
                        'sync_server_iip_error': str(Helpers.now()),
                    })
                    on_error(error)

                StorageService().update_iip(array, on_success_int2, on_error_int2)

            else:
                err = 'Ошибка выгрузки остатков и цен: пустой ответ от сервера'
                self.log(err, True)
                self.update_company({
                    'sync_server_iip_now': False,
                    'sync_server_iip_error': str(Helpers.now()),
                })
                on_error(err)
            pass

        def on_error_int(error):
            self.update_company({
                'sync_server_iip_now': False,
                'sync_server_iip_error': str(Helpers.now()),
            })
            on_error(error)
            pass

        query = []

        items = StorageService().get_items(self.company.ext_id, include_iip=True)

        items_raw = []

        if not items:
            error = 'Ошибка получения товаров из временной базы'
            self.log(error, True)
            on_error_int(error)
            return

        for item in items:
            item_query = obj()
            item_query.itemId = item.item_ext_id
            item_query.points = []
            for iip in item.iip:
                if not iip.int_price == iip.ext_price or not iip.int_count == iip.ext_count:
                    point = obj()
                    point.pointOfSaleId = iip.point_ext_id

                    if iip.int_count is not None and not iip.int_count == iip.ext_count:
                        point.count = iip.int_count
                    if iip.int_price is not None and not iip.int_price == iip.ext_price:
                        point.price = iip.int_price

                    if point.count is not None or point.price is not None:
                        item_query.points.append(point)
                        # need for help fill answer items
                        items_raw.append(obj({
                            'id': iip.iip_ext_id,
                            'itemId': iip.item_ext_id,
                            'pointOfSaleId': iip.point_ext_id,
                            'item_id_internal': iip.item_id_internal,
                            'point_id_internal': iip.point_id_internal,
                        }))

            if len(item_query.points) > 0:
                query.append(item_query)

        if len(query) > 0:
            ApiService().upload_amounts(query, on_success_int, on_error_int)
        else:
            self.log('Остатки и цены не нуждаются в обновлении (изменений не обнаружено)')
            self.update_company({
                'sync_server_iip_now': False,
                # 'sync_server_iip': str(Helpers.now()),
            })
            on_success(True)

    def work(self):
        # company = StorageService().get_company(self.company.ext_inn)
        if not self.company:
            self.log('Компания не найдена при проверке задач', is_error=True)
            return False

        if not self.company.int_enable or not self.company.ext_enable:
            return

        main_next = Helpers.parse_date(self.company.sync_main_next)

        result = obj({'result': None})  # None - if not changed

        if not main_next or Helpers.now() > main_next:
            try:
                wait_loop = QEventLoop()

                self.update_company({
                    'sync_main_now': True,
                })

                self.log('Начинаю полную синхронизацию')
                if self.connect():
                    self.log('Соединение с источником успешно установлено', is_success=True)
                else:
                    raise Exception('Ошибка установки соединения. Проверьте логин и пароль или путь к базе/файлу')

                def on_done():
                    self.log('Синхронизация товаров, точек продаж и выгрузка остатков успешно завершена',
                             is_success=True)
                    result.status = True
                    wait_loop.exit()

                def on_error(text=None):
                    if text:
                        self.log(text, is_error=True)
                    self.log('Задача завершена с ошибкой', is_error=True)
                    result.status = False
                    wait_loop.exit()

                self.sync_items_from_server(
                    lambda q: self.sync_items_from_source(
                        lambda w: self.sync_points_from_server(
                            lambda e: self.sync_points_from_source(
                                lambda r: self.sync_iip_from_source(
                                    lambda t: self.upload_iip_to_server(
                                        lambda y: on_done(),
                                        lambda y: on_error()),
                                    lambda t: on_error()),
                                lambda r: on_error()),
                            lambda e: on_error()),
                        lambda w: on_error()),
                    lambda q: on_error())

                wait_loop.exec_()
            except Exception as error:
                self.log('Задача завершена с ошибкой: {}'.format(error), is_error=True)
                result.status = False

        if result.status == True:
            self.update_company({"sync_main_now": False,
                                 "sync_main": str(Helpers.now()),
                                 "sync_main_next": str(Helpers.now() + timedelta(seconds=Constants.PERIOD_ITEMS))})
        elif result.status == False:
            self.update_company({"sync_main_now": False,
                                 "sync_main_error": str(Helpers.now()),
                                 "sync_main_next": str(Helpers.now() + timedelta(seconds=Constants.PERIOD_ITEMS_ERROR))})

        return result.status

        pass

    def update_company(self, company_dict):
        for key in company_dict:
            self.company.__dict__[key] = company_dict[key]
        company_dict['ext_id'] = self.company.ext_id
        StorageService().update_company(company_dict)
        self.parent.on_update.emit(obj())

    def is_type_price_required(self):
        return self.connector and self.connector.is_type_price_required

    def save_1c_com(self, name):
        if name != self.company.int_1c_com:
            self.company.int_1c_com = name
            self.update_company({"int_1c_com": name})