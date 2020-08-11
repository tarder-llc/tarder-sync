# coding=cp1251
import winreg
from inspect import getmembers

import pythoncom
import win32com.client
import win32con

from app.shared.constants import Constants
from app.shared.helpers import obj, Helpers


class Connector1c:
    is_type_price_required = True

    company = None

    com = None
    connection = None

    def __init__(self, parent, company):
        super(Connector1c, self).__init__()
        self.company = company
        self.parent = parent

    def connect(self):
        pythoncom.CoInitialize()

        connection_string = ''
        if self.company.int_con_type == 0:  # file
            if not self.company.int_base_path:
                return False
            connection_string = 'File="' + str(self.company.int_base_path) + '";'
        elif self.company.int_con_type == 1:  # server
            if not self.company.int_server_name or not self.company.int_base_name:
                return False
            connection_string = 'Srvr="' + str(self.company.int_server_name) + '";Ref="' + str(self.company.int_base_name) + '"'

        connection_string += 'Usr="' + str(self.company.int_base_login) + '";Pwd="' + str(self.company.int_base_password) + '";'

        # 'V83.Application', 'V83c.Application', 'V82.Application', 'V82c.Application', 'V81.Application', 'V81c.Application',
        # 'V83COMConnector', 'V82COMConnector', 'V81COMConnector', 'V83COMConnector.1', 'V82COMConnector.1', 'V81COMConnector.1',
        list_com_names = ['V83.COMConnector', 'V82.COMConnector', 'V81.COMConnector',
                          'V83.COMConnector.1', 'V82.COMConnector.1', 'V81.COMConnector.1']

        list_com_from_system = self.get_com_connectors()

        if list_com_from_system:
            list_com_names = list_com_from_system + list_com_names

        if self.company.int_1c_com:
            Helpers.remove_from_array(list_com_names, self.company.int_1c_com)
            list_com_names.insert(0, self.company.int_1c_com)

        already_created_connections = False

        while len(list_com_names) != 0:
            name = list_com_names[0]
            try:
                self.parent.log('Пытаюсь соединиться по COM: {}'.format(name))
                self.com = win32com.client.Dispatch(name)
                self.connection = self.com.Connect(connection_string)
                if not self.connection:
                    raise Exception('Не удалось подключиться')
                self.parent.save_1c_com(name)
                list_com_names.clear()
            except Exception as err:
                if err.hresult == -2147352567:
                    if hasattr(err, 'excepinfo'):
                        error_text = str(err.excepinfo)
                    else:
                        error_text = 'Возможно нет ЛИЦЕНЗИИ для запуска 1С или установленная версия не подходит для указанной базы данных'
                    self.parent.log('Для коннектора "{}" возникла ошибка: {}'.format(name, error_text), is_error=True)
                    # breakpip install pyinstaller
                else:
                    self.parent.log('COM объект {} не подходит для данной версии 1С'.format(name))

                Helpers.remove_from_array(list_com_names, name)
                if already_created_connections == False and len(list_com_names) == 0:
                    already_created_connections = True
                    self.parent.log('Попробую создать соединения для установленных версий 1С')
                    list_com_names_created = self.create_com_connectors()
                    if list_com_names_created:
                        list_com_names = list_com_names_created

        if not self.connection:
            self.parent.log('Похоже у вас возникли трудности с подключением, если это не ошибка "нехватки лицензий" '
                            'или вы пытаетесь подключиться к 1с после переустановки 1с программы - запустите Tarder Sync '
                            'через правую кнопку мыши с правами администратора и попробуйте снова соединиться вручную - '
                            'будут созданы новые подключения в системе. Это должно сработать.')

        # self.print_members("V83_COMConnector_8_3_12_1714")
        if self.company.int_1c_type == Constants.TYPE_1C_AUTO:
            self.detect_1c_type()
        return self.connection

    def get_com_connectors(self):
        try:
            self.parent.log('Пытаюсь получить COM коннекторы из вашей системы')
            self.com = win32com.client.Dispatch('COMAdmin.COMAdminCatalog')
            apps = self.com.GetCollection("Applications")
            apps.Populate()
            array = []
            for comp in apps:
                print('Name: {}, Key: {}'.format(comp.Name, comp.Key))
                if 'V8' in comp.Name and 'onnector' in comp.Name:
                    array.append(comp.Name)

            return array
        except Exception as err:
            self.parent.log('Ошибка получения коннекторов из вашей системы: {}'.format(err), is_error=True)

    def create_com_connectors(self):
        try:
            self.parent.log('Ищу доступные платформы 1С')
            array_for_create = []

            def find_in_reg(hive, flag):
                a_reg = winreg.ConnectRegistry(None, hive)
                a_key = winreg.OpenKey(a_reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, win32con.KEY_READ | flag)

                count_subkey = winreg.QueryInfoKey(a_key)[0]
                for i in range(count_subkey):
                    try:
                        a_subkey_name = winreg.EnumKey(a_key, i)
                        a_subkey = winreg.OpenKey(a_key, a_subkey_name)
                        reg_name = winreg.QueryValueEx(a_subkey, "DisplayName")[0]
                        if '1C:Предприятие' in reg_name:
                            reg_version = winreg.QueryValueEx(a_subkey, "DisplayVersion")[0]
                            reg_location = winreg.QueryValueEx(a_subkey, "InstallLocation")[0]
                            version = reg_version.replace('.', '_')
                            if flag == win32con.KEY_WOW64_32KEY:
                                bit = '32'
                            elif flag == win32con.KEY_WOW64_64KEY:
                                bit = '64'
                            else:
                                bit = ''
                            name = 'V8_COMConnector_{}_x{}'.format(version, bit)
                            path = '{}bin\comcntr.dll'.format(reg_location)
                            platform = '{}{}'.format(version.split('_')[0], version.split('_')[1])
                            array_for_create.append(obj({
                                'name': name,
                                'path': path,
                                'platform': platform
                            }))
                    except EnvironmentError:
                        continue

            find_in_reg(win32con.HKEY_LOCAL_MACHINE, win32con.KEY_WOW64_32KEY)
            find_in_reg(win32con.HKEY_LOCAL_MACHINE, win32con.KEY_WOW64_64KEY)
            find_in_reg(win32con.HKEY_CURRENT_USER, 0)

            if len(array_for_create) == 0:
                self.parent.log('Не найденно установленных программ 1С предприятия', is_error=True)
                return False

            self.parent.log('Найдено {} платформы'.format(str(len(array_for_create))))

            self.parent.log('Пытаюсь создать COM коннекторы для каждой найденной платформы')
            self.com = win32com.client.Dispatch('COMAdmin.COMAdminCatalog')
            apps = self.com.GetCollection("Applications")
            apps.Populate()
            array = []
            for comp in apps:
                # print('Name: {}, Key: {}'.format(comp.Name, comp.Key))
                if 'V8' in comp.Name and 'onnector' in comp.Name:
                    connector_exist = next((x for x in array_for_create if x.name == comp.Name), None)
                    if connector_exist:
                        Helpers.remove_from_array(array_for_create, connector_exist)

            for item in array_for_create:
                try:
                    new_connector = apps.Add()
                    new_connector.SetValue("Name", item.name)
                    new_connector.SetValue("ApplicationAccessChecksEnabled", 0)
                    # new_connector.SetValue("Identity", 'nt authority\localservice')
                    apps.SaveChanges()
                    result_install = self.com.InstallComponent(new_connector.Value('ID'), item.path, "", "")
                    results = apps.SaveChanges()
                    result_alias = self.com.AliasComponent(new_connector.Value('ID'), 'V{}.COMConnector.1'.format(item.platform),
                                                           "", new_connector.Value('Name'), "")

                    self.parent.log('Коннектор "{}" создан'.format(item.name))
                    array.append(item.name)
                except Exception as err:
                    self.parent.log('Ошибка создания коннектора для "{}" : {}'.format(item.name, err), is_error=True)


            return array
        except Exception as err:
            self.parent.log('Ошибка создания коннекторов в вашей системе: {}'.format(err), is_error=True)


    def disconnect(self):
        if self.connection is not None:
            del self.com
            del self.connection

    def is_connected(self):
        return self.connection is not None

    def detect_1c_type(self):
        if not self.connection:
            return
        name = self.connection.Метаданные.Имя.lower()

        if 'розница' in name:
            self.company.int_1c_type = Constants.TYPE_1C_RETAIL
        elif 'управлениеторговлей' in name:
            self.company.int_1c_type = Constants.TYPE_1C_TRADE
        elif 'бухгалтерия' in name:
            self.company.int_1c_type = Constants.TYPE_1C_BUH

    def print_members(self, obj_name="placeholder_name"):
        """Print members of given COM object"""
        try:
            com_object = win32com.client.gencache.EnsureDispatch(obj_name)
            fields = list(com_object._prop_map_get_.keys())
        except AttributeError:
            print("Object has no attribute '_prop_map_get_'")
            print("Check if the initial COM object was created with"
                  "'win32com.client.gencache.EnsureDispatch()'")
            raise
        methods = [m[0] for m in getmembers(com_object) if (not m[0].startswith("_")
                                                            and "clsid" not in m[0].lower())]

        if len(fields) + len(methods) > 0:
            print("Members of '{}' ({}):".format(obj_name, com_object))
        else:
            raise ValueError("Object has no members to print")

        print("\tFields:")
        if fields:
            for field in fields:
                print(f"\t\t{field}")
        else:
            print("\t\tObject has no fields to print")

        print("\tMethods:")
        if methods:
            for method in methods:
                print(f"\t\t{method}")
        else:
            print("\t\tObject has no methods to print")

    def get_company(self):
        q = '''
                ВЫБРАТЬ
                  Организации.Наименование КАК name,
                  Организации.ИНН КАК inn
                ИЗ
                  Справочник.Организации КАК Организации
                ГДЕ
                    Организации.ИНН = &ИНН
                '''

        query = self.connection.NewObject("Query", q)

        query.SetParameter("ИНН", self.company.ext_inn)
        res = query.Execute().Choose()

        if res.next():
            company = obj({
                'int_name': str(res.name),
                'int_inn': str(res.inn),
            })
            return company
        else:
            return False

    def get_items(self, array_ids):
        q = '''
                ВЫБРАТЬ
                  Номенклатура.Наименование КАК name,
                  Номенклатура.Код КАК code
                ИЗ
                  Справочник.Номенклатура КАК Номенклатура
                ГДЕ
                    Номенклатура.Код В (&СписокКодов)
                '''
        # q.format(", ".join(map("{}".format, arrayIds)))
        query = self.connection.NewObject("Query", q)
        list_ids = self.connection.NewObject("Array")
        for value in array_ids:
            list_ids.add(value)

        query.SetParameter("СписокКодов", list_ids)
        res = query.Execute().Choose()

        items = []
        while res.next():
            item = obj({
                'int_id': str(res.code),
                'int_name': str(res.name),
            })
            items.append(item)

        return items

    def get_points(self, array_ids):

        if self.company.int_1c_type == Constants.TYPE_1C_TRADE:  # no code exist, id is 'name'
            q = '''
                    ВЫБРАТЬ
                        Склад.Наименование КАК name,
                        Склад.Наименование КАК code
                    ИЗ
                        Справочник.Склады КАК Склад
                    ГДЕ
                        Склад.Код В (&СписокКодов)
                '''
        else:
            q = '''
                    ВЫБРАТЬ
                        Склад.Наименование КАК name,
                        Склад.Код КАК code
                    ИЗ
                        Справочник.Склады КАК Склад
                    ГДЕ
                        Склад.Код В (&СписокКодов)
                '''

        query = self.connection.NewObject("Query", q)
        list_ids = self.connection.NewObject("Array")
        for value in array_ids:
            list_ids.add(value)

        query.SetParameter("СписокКодов", list_ids)
        res = query.Execute().Choose()

        items = []
        while res.next():
            item = obj({
                'int_id': str(res.code),
                'int_name': str(res.name),
            })
            items.append(item)

        return items

    def get_types_of_prices(self):

        if self.company.int_1c_type == Constants.TYPE_1C_BUH:
            q = '''
                    ВЫБРАТЬ
                      Цена.Наименование КАК name
                    ИЗ
                      Справочник.ТипыЦенНоменклатуры КАК Цена
                    '''
        else:
            q = '''
                    ВЫБРАТЬ
                      Цена.Наименование КАК name
                    ИЗ
                      Справочник.ВидыЦен КАК Цена
                    '''

        query = self.connection.NewObject("Query", q)
        res = query.Execute().Choose()

        items = []
        while res.next():
            item = obj({
                'int_price_name': res.name
            })
            items.append(item)

        return items

    def get_count_and_price_in_points(self, item_ids, point_ids, type_price):

        item_codes = []

        # detaching characteristics
        for item_id in item_ids:
            value = item_id
            if "___" in value:
                value = value.split("___")[0]
            item_codes.append(value)

        if self.company.int_1c_type == Constants.TYPE_1C_TRADE:
            q = '''
ВЫБРАТЬ
    СпрНоменклатура.Код КАК item_id,
    ОстаткиТоваров.Склад.Наименование КАК point_id,
    ОстаткиТоваров.ВНаличииОстаток КАК int_count,
    ЦеныНоменклатуры.Цена КАК int_price,
    ЦеныНоменклатуры.Характеристика.Наименование КАК char_name_price,
    ОстаткиТоваров.Характеристика.Наименование КАК char_name_count
ИЗ
    Справочник.Номенклатура КАК СпрНоменклатура
ЛЕВОЕ СОЕДИНЕНИЕ РегистрНакопления.ТоварыНаСкладах.Остатки(, Склад.Наименование В (&СписокСкладов)) КАК ОстаткиТоваров
    ПО (СпрНоменклатура.Ссылка = ОстаткиТоваров.Номенклатура)
ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ЦеныНоменклатуры.СрезПоследних(, ВидЦены.Наименование = &ВидЦены {price_query}) КАК ЦеныНоменклатуры
    ПО (СпрНоменклатура.Ссылка = ЦеныНоменклатуры.Номенклатура)
ГДЕ
    СпрНоменклатура.Код В (&СписокКодов)
                '''
        elif self.company.int_1c_type == Constants.TYPE_1C_BUH:
            q = '''
ВЫБРАТЬ
	СпрНоменклатура.Ссылка,
	СпрНоменклатура.Код КАК item_id,
	ОстаткиТоваров.Субконто2.Код КАК point_id, 
	ОстаткиТоваров.КоличествоОстаток КАК int_count,
    ЦеныНоменклатуры.Цена КАК int_price
ИЗ
	Справочник.Номенклатура КАК СпрНоменклатура
	
ЛЕВОЕ СОЕДИНЕНИЕ РегистрБухгалтерии.Хозрасчетный.Остатки(, Счет.Код В ИЕРАРХИИ (&Счета), 
                                                    &ВидыСубконто, Субконто2.Код В (&СписокСкладов) ) КАК ОстаткиТоваров
	ПО СпрНоменклатура.Ссылка = ОстаткиТоваров.Субконто1

ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ЦеныНоменклатуры.СрезПоследних(, ТипЦен.Наименование=&ВидЦены) КАК ЦеныНоменклатуры
    ПО (СпрНоменклатура.Ссылка = ЦеныНоменклатуры.Номенклатура)
ГДЕ
    СпрНоменклатура.Код В (&СписокКодов)
                '''
        else:  # Retail and other
            q = '''
ВЫБРАТЬ
    СпрНоменклатура.Код КАК item_id,
    ОстаткиТоваров.Склад.Код КАК point_id,
    ОстаткиТоваров.КоличествоОстаток КАК int_count,
    ЦеныНоменклатуры.Цена КАК int_price,
    ЦеныНоменклатуры.Характеристика.Наименование КАК char_name_price,
    ОстаткиТоваров.Характеристика.Наименование КАК char_name_count
ИЗ
    Справочник.Номенклатура КАК СпрНоменклатура
ЛЕВОЕ СОЕДИНЕНИЕ РегистрНакопления.ТоварыНаСкладах.Остатки(, Склад.Код В (&СписокСкладов)) КАК ОстаткиТоваров
    ПО (СпрНоменклатура.Ссылка = ОстаткиТоваров.Номенклатура)
ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ЦеныНоменклатуры.СрезПоследних(, ВидЦены.Наименование = &ВидЦены) КАК ЦеныНоменклатуры
    ПО (СпрНоменклатура.Ссылка = ЦеныНоменклатуры.Номенклатура)
ГДЕ
    СпрНоменклатура.Код В (&СписокКодов)
                '''

        query = self.connection.NewObject("Query", q)

        # item ids
        list_item_ids = self.connection.NewObject("Array")
        for value in item_codes:
            list_item_ids.add(value)
        query.SetParameter("СписокКодов", list_item_ids)

        # point ids
        list_point_ids = self.connection.NewObject("Array")
        for value in point_ids:
            list_point_ids.add(value)
        query.SetParameter("СписокСкладов", list_point_ids)

        # type of price
        query.SetParameter("ВидЦены", '{}'.format(type_price))

        if self.company.int_1c_type == Constants.TYPE_1C_BUH:
            list_subkonto_ids = self.connection.NewObject("Array")
            list_subkonto_ids.add(self.connection.ПланыВидовХарактеристик.ВидыСубконтоХозрасчетные.Номенклатура)
            list_subkonto_ids.add(self.connection.ПланыВидовХарактеристик.ВидыСубконтоХозрасчетные.Склады)
            query.SetParameter("ВидыСубконто", list_subkonto_ids)

            list_subkonto_ids = self.connection.NewObject("Array")
            list_subkonto_ids.add('41.01')
            query.SetParameter("Счета", list_subkonto_ids)

        res = query.Execute().Choose()

        items = []

        while res.next():

            if res.int_price is not None:
                for point_id in point_ids:  # the price is the same for all warehouses
                    item = obj()
                    if self.company.int_1c_type == Constants.TYPE_1C_BUH:
                        item.item_id_internal = res.item_id
                    else:
                        item.item_id_internal = Helpers.get_separator(res.item_id, res.char_name_price)

                    item.point_id_internal = point_id
                    item.int_price = Helpers.convert_number(res.int_price, False)

                    item_exist = next(filter(lambda x:
                                             x.item_id_internal == item.item_id_internal
                                             and x.point_id_internal == item.point_id_internal, items), None)

                    if not item_exist:
                        items.append(item)
                    else:
                        item_exist.int_price = item.int_price

            if res.int_count is not None:
                item = obj()
                if self.company.int_1c_type == Constants.TYPE_1C_BUH:
                    item.item_id_internal = res.item_id
                else:
                    item.item_id_internal = Helpers.get_separator(res.item_id, res.char_name_count)
                item.point_id_internal = res.point_id
                item.int_count = Helpers.convert_number(res.int_count, False)

                item_exist = next(filter(lambda x:
                                         x.item_id_internal == item.item_id_internal
                                         and x.point_id_internal == item.point_id_internal, items), None)

                if not item_exist:
                    items.append(item)
                else:
                    item_exist.int_count = item.int_count

        return items
