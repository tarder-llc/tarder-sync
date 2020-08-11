import csv
import io
import os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QTimer, Signal
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QVBoxLayout

from app.parts.company.company_ui import Ui_Form
from app.shared.constants import Constants
from app.shared.helpers import Helpers, obj
from app.shared.main_service import MainService
from app.shared.storage_service import StorageService
from app.shared.text_logger import TextLogger
from app.shared.variables import Variables
from app.worker import Worker


class CompanyComponent(QWidget):
    connection = None
    ui = None

    company = None
    on_update = Signal(list)

    def __init__(self, parent, company):
        super(CompanyComponent, self).__init__(parent)
        if Variables().isDebug:
            self.ui = Helpers.get_ui(__file__)  # just load ui file
            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.ui)
        else:
            self.ui = Ui_Form()
            self.ui.setupUi(self)  # load class from converted ui file

        self.parent = parent
        self.company = company
        self.on_update.connect(self.update_company)
        self.worker = Worker(self, self.company)
        self.init()

    def init(self):
        self.ui.select_path_b.clicked.connect(self.open_select_path_1c)
        self.ui.connect_to_1c_b.clicked.connect(self.connect_to_source)

        self.ui.find_company_b.clicked.connect(self.find_company_in_source)
        self.ui.sync_all_b.clicked.connect(self.sync_all)

        self.ui.sync_with_tarder_items_b.clicked.connect(self.sync_with_tarder_items)
        self.ui.sync_with_source_items_b.clicked.connect(self.sync_with_source_items)

        self.ui.sync_with_tarder_points_b.clicked.connect(self.sync_with_tarder_points)
        self.ui.sync_with_source_points_b.clicked.connect(self.sync_with_source_points)

        self.ui.sync_with_source_iip_b.clicked.connect(self.sync_with_source_iip)
        self.ui.upload_to_tarder_iip_b.clicked.connect(self.upload_to_tarder_iip)

        # self.ui.save_changes_b.clicked.connect(self.save_changes)
        self.ui.undo_changes_b.clicked.connect(self.reload_company)
        self.ui.toggle_active_worker_b.clicked.connect(self.toggle_worker)

        self.ui.select_path_excel_b.clicked.connect(self.open_select_path_xls)
        self.ui.select_path_csv_b.clicked.connect(self.open_select_path_csv)

        self.ui.connect_to_xls_b.clicked.connect(self.connect_to_source)
        self.ui.connect_to_csv_b.clicked.connect(self.connect_to_source)

        self.ui.company_tabs.currentChanged.connect(self.company_tab_changed)

        # Set up logging
        self.logging = TextLogger(self.ui.log_text, self.company).log

        # where do we get information from
        self.ui.type_source.clear()
        self.ui.type_source.addItem('1С Предприятие', 0)
        self.ui.type_source.addItem('Excel файл', 1)
        self.ui.type_source.addItem('CSV файл', 2)
        self.ui.type_source.currentIndexChanged.connect(self.on_update_source_type)

        self.ui.con_type.clear()
        self.ui.con_type.addItem('Файловая версия', Constants.CONNECTION_TYPE_1C_FILE)
        self.ui.con_type.addItem('Серверная версия', Constants.CONNECTION_TYPE_1C_SERVER)
        self.ui.con_type.currentIndexChanged.connect(self.on_update_connection_type)

        self.ui.type_1c.clear()
        self.ui.type_1c.addItem('Автоопределение', Constants.TYPE_1C_AUTO)
        self.ui.type_1c.addItem('Розница', Constants.TYPE_1C_RETAIL)
        self.ui.type_1c.addItem('Управление торговлей', Constants.TYPE_1C_TRADE)
        self.ui.type_1c.addItem('Бухгалтерия', Constants.TYPE_1C_BUH)
        self.ui.type_1c.currentIndexChanged.connect(self.on_update_1c_type)

        self.ui.company_tabs.setCurrentIndex(Constants.COMPANY_TAB_LOG)

        self.ui.items_table.installEventFilter(self)
        self.ui.points_table.installEventFilter(self)
        self.ui.item_in_points_table.installEventFilter(self)

        self.fill_view()

        # self.refresh_company_data(self.company,
        #                                    lambda x: self.refresh_table(),
        #                                    lambda x: self.refresh_table())

    def fill_view(self):
        # fill values

        self.ui.type_source.setCurrentIndex(self.company.int_source_type)
        self.check_company_sync()

        # self.ui.type_source.setCurrentIndex(self.company.int_source_type)
        self.on_update_source_type(self.company.int_source_type)

        self.ui.company_inn_value.setText(self.company.ext_inn)
        self.ui.server_name.setText(self.company.int_server_name)
        self.ui.base_name.setText(self.company.int_base_name)
        self.ui.select_path_value.setText(self.company.int_base_path)
        self.ui.base_login.setText(self.company.int_base_login)
        self.ui.base_password.setText(self.company.int_base_password)

        self.ui.select_path_excel_value.setText(self.company.int_file_path)
        self.ui.select_path_csv_value.setText(self.company.int_file_path)

        if self.company.int_type_price:
            index = self.ui.price_type.findText(self.company.int_type_price)
            if index > -1:
                self.ui.price_type.setCurrentIndex(index)
            else:
                self.ui.price_type.addItem(self.company.int_type_price)
                self.ui.price_type.setCurrentIndex(self.ui.price_type.count() - 1)


        # active / inactive
        self.ui.toggle_active_worker_b.setToolTip(None)
        if not self.company.ext_enable:
            self.ui.toggle_active_worker_b.setText('Выключен в виртуальном офисе')
            self.ui.toggle_active_worker_b.setToolTip('Зайдите в виртуальный офис через браузер под владельцем'
                                                      ' организации в меню "Настройки" и включите синхронизацию '
                                                      'для этой компании')
            self.ui.toggle_active_worker_b.setEnabled(False)
            enabled_actions = False
        elif self.company.int_enable:
            self.ui.toggle_active_worker_b.setText('Остановить автообмен')
            self.ui.toggle_active_worker_b.setEnabled(True)
            enabled_actions = False
        else:
            self.ui.toggle_active_worker_b.setText('Сохранить изменения и запустить автообмен')
            self.ui.toggle_active_worker_b.setEnabled(True)
            enabled_actions = True

        self.ui.container_top.setEnabled(enabled_actions)
        self.ui.container_1c.setEnabled(enabled_actions)
        self.ui.container_excel.setEnabled(enabled_actions)
        self.ui.container_csv.setEnabled(enabled_actions)
        self.ui.undo_changes_b.setEnabled(enabled_actions)
        self.ui.type_source.setEnabled(enabled_actions)
        self.ui.container_control.setEnabled(enabled_actions)
        self.ui.sync_with_tarder_items_b.setEnabled(enabled_actions)
        self.ui.sync_with_source_items_b.setEnabled(enabled_actions)
        self.ui.sync_with_tarder_points_b.setEnabled(enabled_actions)
        self.ui.sync_with_source_points_b.setEnabled(enabled_actions)
        self.ui.price_type.setEnabled(enabled_actions)
        self.ui.sync_with_source_iip_b.setEnabled(enabled_actions)
        self.ui.upload_to_tarder_iip_b.setEnabled(enabled_actions)


    def load_from_view(self):
        # fill values to company

        self.company.int_source_type = self.ui.type_source.currentIndex()
        self.company.int_con_type = self.ui.con_type.currentIndex()
        self.company.int_1c_type = self.ui.type_1c.currentIndex()
        self.company.int_type_price = self.ui.price_type.currentText()
        if self.company.int_type_price == '':
            self.company.int_type_price = None

        self.company.ext_inn = self.ui.company_inn_value.text()
        self.company.int_server_name = self.ui.server_name.text()
        self.company.int_base_name = self.ui.base_name.text()
        self.company.int_base_path = self.ui.select_path_value.text()
        self.company.int_base_login = self.ui.base_login.text()
        self.company.int_base_password = self.ui.base_password.text()

    def save_changes(self):
        def on_success_int(result):
            self.log('Изменения сохранены', is_success=True)
            pass

        def on_error_int(err):
            self.log('Возникла ошибка при созранении изменений', is_error=True)
            pass

        self.load_from_view()
        return StorageService().update_company(self.company.__dict__, on_success_int, on_error_int)

    def reload_company(self):

        company = StorageService().get_company(self.company.ext_inn)

        if company:
            self.log('Компания загружена из временной базы', is_success=True)
            self.company = company
            self.worker.company = company
            self.fill_view()
        else:
            self.log('Компания не найдена в временной базы - попробуйте перелогиниться', is_error=True)

    def company_tab_changed(self, index):
        if index == Constants.COMPANY_TAB_ITEMS:
            self.refresh_table_items()
        elif index == Constants.COMPANY_TAB_POINTS:
            self.refresh_table_points()
        elif index == Constants.COMPANY_TAB_ITEM_IN_POINTS:
            self.refresh_table_iip()
            if self.worker.is_type_price_required() and self.company.int_type_price is None:
                self.load_types_of_price()
        pass

    def sync_all(self):
        self.connect_to_source()
        # self.sync_with_tarder_items()
        # self.ui.company_tabs.setCurrentIndex(1)
        # QTimer().singleShot(1000, self.sync_with_source_items)
        self.ui.company_tabs.setCurrentIndex(Constants.COMPANY_TAB_LOG)
        # self.refresh_table_iip()

        QTimer().singleShot(1000,
                            lambda: self.sync_with_tarder_items(
                                lambda q: self.sync_with_source_items(
                                    lambda w: self.sync_with_tarder_points(
                                        lambda e: self.sync_with_source_points(
                                            lambda r: self.sync_with_source_iip(
                                                lambda t: self.upload_to_tarder_iip(
                                                    lambda y: self.log('Полная синхронизация успешно завершена',
                                                                       is_success=True)
                                                )))))))

    def open_select_path_1c(self):
        result = QFileDialog.getExistingDirectory()
        self.ui.select_path_value.setText(result)

    def on_update_source_type(self, index):

        self.ui.container_excel.hide()
        self.ui.container_csv.hide()
        self.ui.container_1c.hide()
        self.ui.company_name_value.hide()
        self.ui.find_company_b.hide()
        self.ui.container_type_of_price.hide()

        self.company.int_source_type = index

        if index == 0:  # 1c
            self.ui.container_1c.show()
            self.ui.company_name_value.show()
            self.ui.find_company_b.show()
            self.ui.container_type_of_price.show()

            self.ui.con_type.setCurrentIndex(self.company.int_con_type)
            self.on_update_connection_type(self.company.int_con_type)

            # where do we get information from
            self.ui.type_1c.setCurrentIndex(self.company.int_1c_type)
            self.on_update_1c_type(self.company.int_1c_type)

        elif index == 1:  # excel
            self.ui.container_excel.show()
        elif index == 2:  # csv
            self.ui.container_csv.show()

    def on_update_1c_type(self, index):
        if not index == -1:
            self.company.int_1c_type = index
        pass

    def on_update_connection_type(self, index):
        self.company.int_con_type = index
        if index == Constants.CONNECTION_TYPE_1C_FILE:
            self.ui.type1c_srv.hide()
            self.ui.type1c_file.show()
        elif index == Constants.CONNECTION_TYPE_1C_SERVER:
            self.ui.type1c_srv.show()
            self.ui.type1c_file.hide()

    def connect_to_source(self):
        self.log('Начинаю подключение к источнику данных')

        self.ui.company_tabs.setCurrentIndex(Constants.COMPANY_TAB_LOG)

        # self.company.int_server_name = self.ui.server_name.text()
        # self.company.int_base_name = self.ui.base_name.text()
        #
        # self.company.int_base_path = self.ui.select_path_value.text()
        # self.company.int_base_login = self.ui.base_login.text()
        # self.company.int_base_password = self.ui.base_password.text()

        self.load_from_view()

        def work():
            if self.worker.connect():
                self.log('Соединение успешно установлено', is_success=True)
                self.load_types_of_price()
            else:
                self.log('Ошибка установки соединения', True)
            self.update_connection_status()
            if self.company.int_1c_type is not None:
                self.ui.type_1c.setCurrentIndex(self.company.int_1c_type)

        QTimer().singleShot(100, work)

    def update_connection_status(self):
        if not self.worker.is_connected:
            self.ui.connection_1c_value.setText('<font color="{}">{}</font>'.format('red', 'Соединение не установлено'))
        else:
            self.ui.connection_1c_value.setText('<font color="{}">{}</font>'.format('green', 'Соединение установлено'))

    def log(self, text, is_error=False, is_success=False):
        text = "[ {} ] {}".format(self.company.ext_name, text)
        if is_error:
            self.logging.error(text)
        elif is_success:
            self.logging.log(Constants.LOG_GOOD, text)
        else:
            self.logging.info(text)
        pass

    # COMPANY

    def check_company_sync(self, is_checked=False):
        if self.company.int_inn:
            self.ui.company_name_value.setText('Компания найдена: ' + self.company.int_name)
            self.ui.company_name_value.setStyleSheet('color: green')
        else:
            if is_checked:
                self.ui.company_name_value.setText('Компания с данным ИНН не найдена в указанном источнике')
                self.ui.company_name_value.setStyleSheet('color: red')
            else:
                self.ui.company_name_value.setText('Вы можете найти компанию в указанном источнике данных')
                self.ui.company_name_value.setStyleSheet('color: grey')

    def find_company_in_source(self):
        def on_success_int(result):
            self.log('Компания найдена в источнике', is_success=True)
            self.check_company_sync(is_checked=True)
            pass

        def on_error_int(err):
            self.log('Возникла ошибка при поиске компании')
            self.check_company_sync(is_checked=True)
            pass

        self.worker.find_company_in_source(on_success_int, on_error_int)

    # ITEMS

    def sync_with_tarder_items(self, on_success=lambda x: x, on_error=lambda x: x):
        self.log('Начинаю ручную синхронизацию товаров')

        def on_success_int(result):
            self.log('Товары успешено обновлены из Tarder', is_success=True)
            self.refresh_table_items()
            on_success(result)
            pass

        def on_error_int(err):
            self.log('Возникла ошибка при загрузке товаров из Tarder', True)
            self.refresh_table_items()
            on_error(err)
            pass

        self.worker.sync_items_from_server(on_success_int, on_error_int)

    def sync_with_source_items(self, on_success=lambda x: x, on_error=lambda x: x):
        # if not self.worker.is_connected:
        #     self.log('Сначала подключитесь к источнику данных!', True)
        #     return

        self.log('Начинаю загрузку товаров из источника')

        def on_success_int(result):
            self.log('Товары успешено обновлены из источника', is_success=True)
            self.refresh_table_items()
            on_success(result)
            pass

        def on_error_int(err):
            self.log('Возникла ошибка при загрузке товаров из источника', True)
            self.refresh_table_items()
            on_error(err)
            pass

        self.worker.sync_items_from_source(on_success_int, on_error_int)

    def refresh_table_items(self, mark_error=True):
        # self.log('Обновляю таблицу товаров из временной базы...')

        self.ui.items_table.clearContents()
        self.ui.items_table.setRowCount(0)

        items = StorageService().get_items(self.company.ext_id)

        if not items:
            self.log('Ошибка получения товаров из временной базы', True)
            return

        for item in items:
            # insert new row at the end of the tableWidget
            row_number = self.ui.items_table.rowCount()
            self.ui.items_table.insertRow(row_number)
            self.ui.items_table.setItem(row_number, 0, QTableWidgetItem(item.ext_id))
            self.ui.items_table.setItem(row_number, 1, QTableWidgetItem(item.ext_name))
            self.ui.items_table.setItem(row_number, 2, QTableWidgetItem(item.ext_sku))
            ext_id_internal = QTableWidgetItem(item.ext_id_internal)
            int_id = QTableWidgetItem(item.int_id)
            if mark_error:
                if not item.ext_id_internal:
                    ext_id_internal.setBackgroundColor(QColor('#bf5656'))
                    ext_id_internal.setToolTip('Необходимо указать внутренний ID в виртуальном офисе Tarder')
                    pass
                elif item.ext_id_internal == item.int_id:
                    int_id.setBackgroundColor(QColor('#66bf62'))
                else:
                    int_id.setBackgroundColor(QColor('#bf5656'))
                    int_id.setToolTip('У товара указан внутренний ID, но он не найден в источнике')

            self.ui.items_table.setItem(row_number, 3, ext_id_internal)
            self.ui.items_table.setItem(row_number, 4, int_id)
            self.ui.items_table.setItem(row_number, 5, QTableWidgetItem(item.int_name))

        self.log('Таблица товаров обновлена')
        pass

    # POINT OF SALES

    def sync_with_tarder_points(self, on_success=lambda x: x, on_error=lambda x: x):
        self.log('Начинаю ручную синхронизацию точек продаж')

        def on_success_int(result):
            self.refresh_table_points()
            on_success(result)

        def on_error_int(err):
            self.refresh_table_points()
            on_error(err)

        self.worker.sync_points_from_server(on_success_int, on_error_int)

    def sync_with_source_points(self, on_success=lambda x: x, on_error=lambda x: x):
        # if not self.worker.is_connected:
        #     self.log('Сначала подключитесь к источнику данных!', True)
        #     return

        self.log('Начинаю загрузку точек продаж из источника')

        def on_success_int(result):
            self.log('Точки продаж успешено обновлены из источника', is_success=True)
            self.refresh_table_points()
            on_success(result)
            pass

        def on_error_int(err):
            self.log('Возникла ошибка при загрузке точек продаж из источника', True)
            self.refresh_table_points()
            on_error(err)
            pass

        self.worker.sync_points_from_source(on_success_int, on_error_int)

    def refresh_table_points(self, mark_error=True):
        # self.log('Обновляю таблицу точек продаж из временной базы...')

        self.ui.points_table.clearContents()
        self.ui.points_table.setRowCount(0)

        items = StorageService().get_points(self.company.ext_id)

        if not items:
            self.log('Точек продаж нет в временной базе', True)
            return

        for item in items:
            # insert new row at the end of the tableWidget
            row_number = self.ui.points_table.rowCount()
            self.ui.points_table.insertRow(row_number)
            self.ui.points_table.setItem(row_number, 0, QTableWidgetItem(item.ext_id))
            self.ui.points_table.setItem(row_number, 1, QTableWidgetItem(item.ext_name))
            ext_id_internal = QTableWidgetItem(item.ext_id_internal)
            int_id = QTableWidgetItem(item.int_id)
            if mark_error:
                if not item.ext_id_internal:
                    ext_id_internal.setBackgroundColor(QColor('#bf5656'))
                    ext_id_internal.setToolTip('Необходимо указать внутренний ID в виртуальном офисе Tarder')
                elif item.ext_id_internal == item.int_id:
                    int_id.setBackgroundColor(QColor('#66bf62'))
                else:
                    int_id.setBackgroundColor(QColor('#bf5656'))
                    int_id.setToolTip('У точки продаж указан внутренний ID, но он не найден в источнике')

            self.ui.points_table.setItem(row_number, 2, ext_id_internal)
            self.ui.points_table.setItem(row_number, 3, int_id)
            self.ui.points_table.setItem(row_number, 4, QTableWidgetItem(item.int_name))

        self.log('Таблица точек продаж обновлена')
        pass

    # TYPES OF PRICE
    def load_types_of_price(self):
        if not self.worker.is_type_price_required():
            # self.log('Типы цен не обязательный для выбранного источника')
            return

        def int_on_success(result):
            self.log('Типы цен загружены из источника')
            self.types_of_price = result
            self.ui.price_type.clear()

            for price in self.types_of_price:
                self.ui.price_type.addItem(price.int_price_name)
                if 'розн' in price.int_price_name.lower():
                    self.select_type_of_price(price.int_price_name)

            check_type_price()

        def int_on_error(err):
            self.log('Возникла ошибка при обновлении типов цен из источника', is_error=True)
            self.ui.price_type.clear()
            check_type_price()
            pass

        def check_type_price():
            if self.company.int_type_price is not None:
                index = self.ui.price_type.findText(self.company.int_type_price)
                if index < 0:
                    self.ui.price_type.addItem(self.company.int_type_price)
                self.ui.price_type.setCurrentIndex(index)

        self.worker.get_types_of_price(int_on_success, int_on_error)

    def select_type_of_price(self, type_price):
        if self.company.int_type_price is None:
            self.company.int_type_price = type_price
            self.ui.price_type.setCurrentIndex(self.ui.price_type.findText(type_price))

    # ITEM IN POINTS

    def sync_with_source_iip(self, on_success=lambda x: x, on_error=lambda x: x):
        # if not self.worker.is_connected:
        #     self.log('Сначала подключитесь к источнику данных!', True)
        #     return

        if self.worker.is_type_price_required() and self.company.int_type_price is None:
            self.log('Не выбран тип цен', True)
            self.load_types_of_price()
            return

        self.log('Начинаю загрузку остатков и цен из источника')
        self.refresh_table_iip()

        def int_on_success(result):
            self.log('Остатки и цены успешено обновлены из источника', is_success=True)
            self.refresh_table_iip()
            on_success(result)
            pass

        def int_on_error(err):
            self.log('Возникла ошибка при обновлении остатков и цен из источника', True)
            self.refresh_table_iip()
            on_error(err)
            pass

        self.worker.sync_iip_from_source(int_on_success, int_on_error)

    def upload_to_tarder_iip(self, on_success=lambda x: x, on_error=lambda x: x):
        # if not self.worker.is_connected:
        #     self.log('Сначала подключитесь к источнику данных!', True)

        self.log('Начинаю выгрузку остатков и цен из временной базы данных')

        def int_on_success(result):
            self.log('Остатки и цены успешено загружены на сервер', is_success=True)
            self.refresh_table_iip()
            on_success(result)
            pass

        def int_on_error(err):
            self.log('Возникла ошибка при загрузкb на сервер', True)
            self.refresh_table_iip()
            on_error(err)
            pass

        self.worker.upload_iip_to_server(int_on_success, int_on_error)

    def refresh_table_iip(self, mark_error=True):
        # self.log('Обновляю таблицу цен и количества из временной базы...')

        self.ui.item_in_points_table.clearContents()
        self.ui.item_in_points_table.setColumnCount(0)

        points = StorageService().get_points(self.company.ext_id)

        self.ui.item_in_points_table.clearContents()
        self.ui.item_in_points_table.horizontalHeader().setVisible(True)
        self.ui.item_in_points_table.verticalHeader().setVisible(True)
        self.ui.item_in_points_table.setColumnCount(4 + len(points) * 2)

        self.ui.item_in_points_table.setHorizontalHeaderItem(0, QTableWidgetItem('ID Tarder'))
        self.ui.item_in_points_table.setHorizontalHeaderItem(1, QTableWidgetItem('SKU Tarder'))
        self.ui.item_in_points_table.setHorizontalHeaderItem(2, QTableWidgetItem('ID Источника'))
        self.ui.item_in_points_table.setHorizontalHeaderItem(3, QTableWidgetItem('Имя Источника'))

        # set columns
        index = 4
        for point in points:
            self.ui.item_in_points_table.setHorizontalHeaderItem(index,
                                                                 QTableWidgetItem('Кол-во {}'.format(point.int_name)))
            index += 1
            self.ui.item_in_points_table.setHorizontalHeaderItem(index,
                                                                 QTableWidgetItem('Цена {}'.format(point.int_name)))
            index += 1

        # set rows
        self.ui.item_in_points_table.setRowCount(0)

        items = StorageService().get_items(self.company.ext_id, include_iip=True)

        if not items:
            self.log('Товаров нет в временной базе, сначала загрузите их из Tarder')
            return

        for item in items:
            # insert new row at the end of the tableWidget
            row_number = self.ui.item_in_points_table.rowCount()
            self.ui.item_in_points_table.insertRow(row_number)
            self.ui.item_in_points_table.setItem(row_number, 0, QTableWidgetItem(item.ext_id))
            self.ui.item_in_points_table.setItem(row_number, 1, QTableWidgetItem(item.ext_sku))
            # ext_id_internal = QTableWidgetItem(item.ext_id_internal)
            int_id = QTableWidgetItem(item.int_id)
            # if mark_error:
            #     if not item.ext_id_internal:
            #         ext_id_internal.setBackgroundColor(QColor('#bf5656'))
            #     elif item.ext_id_internal == item.int_id:
            #         int_id.setBackgroundColor(QColor('#66bf62'))
            #     else:
            #         int_id.setBackgroundColor(QColor('#bf5656'))

            # self.ui.item_in_points_table.setItem(row_number, 2, ext_id_internal)

            if not item.int_id:
                int_id.setBackgroundColor(QColor('#bf5656'))
                int_id.setToolTip('У товара указан внутренний ID, но он не найден в источнике')

            self.ui.item_in_points_table.setItem(row_number, 2, int_id)
            self.ui.item_in_points_table.setItem(row_number, 3, QTableWidgetItem(item.int_name))

            index = 4
            for point in points:
                item_in_point = next(filter(lambda x: x.point_id_internal == point.ext_id_internal, item.iip), obj())

                count = Helpers.convert_number(item_in_point.int_count, True, True)

                point_count = QTableWidgetItem('{}'.format(count or ''))

                if not item.int_id:
                    pass
                elif count is None:
                    point_count.setBackgroundColor(QColor('#bf5656'))
                    point_count.setToolTip('Ошибка загрузки из источника, проверьте существование этих данных в нем')
                elif not item_in_point.int_count == item_in_point.ext_count:
                    point_count.setBackgroundColor(QColor('#4d84b0'))
                    point_count.setToolTip('Поле изменено и будет выгружено на сервер')

                self.ui.item_in_points_table.setItem(row_number, index, point_count)
                index += 1

                price = Helpers.convert_number(item_in_point.int_price, True, True)
                point_price = QTableWidgetItem('{}'.format(price or ''))

                if not item.int_id:
                    pass
                elif price is None:
                    point_price.setBackgroundColor(QColor('#bf5656'))
                    point_price.setToolTip('Ошибка загрузки из источника, проверьте существование этих данных в нем')
                elif not item_in_point.int_price == item_in_point.ext_price:
                    point_price.setBackgroundColor(QColor('#4d84b0'))
                    point_price.setToolTip('Поле изменено и будет выгружено на сервер')

                self.ui.item_in_points_table.setItem(row_number, index, point_price)
                index += 1

        self.log('Таблица цен и количества товара обновлена')
        pass

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
                event.matches(QtGui.QKeySequence.Copy)):
            self.copy_selection(source)
            return True
        return super(QWidget, self).eventFilter(source, event)

    def copy_selection(self, table):
        selection = table.selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            rowcount = rows[-1] - rows[0] + 1
            colcount = columns[-1] - columns[0] + 1
            table = [[''] * colcount for _ in range(rowcount)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - columns[0]
                table[row][column] = index.data()
            stream = io.StringIO()
            csv.writer(stream, delimiter='\t').writerows(table)
            QtWidgets.qApp.clipboard().setText(stream.getvalue())

    def toggle_worker(self):
        if not self.company.int_enable:
            self.load_from_view()
            self.company.int_enable = True
            self.worker.disconnect()

            if not StorageService().update_company(self.company.__dict__):
                self.company.int_enable = False
                self.log('Ошибка при запуске автообмена - сохранение компании', is_error=True)
            else:
                self.log('Автообмен запущен', is_success=True)
            self.fill_view()
        else:
            if StorageService().update_company({"ext_id": self.company.ext_id, "int_enable": False}):
                self.company.int_enable = False
                self.fill_view()
                self.log('Автообмен остановлен', is_success=True)
            else:
                self.log('Ошибка при остановке автообмена - сохранение компании', is_error=True)

    def update_company(self, props=None):
        if props.company is None:
            company = StorageService().get_company(self.company.ext_inn)
        else:
            company = props.company

        if Helpers.copy_fields(company, self.company, ['ext_enable', 'int_enable']):
            self.fill_view()



    def open_select_path_xls(self):
        if self.company.int_file_path:
            path_dir = os.path.dirname(self.company.int_file_path)
        else:
            path_dir = None
        result = QFileDialog.getOpenFileName(self, 'Выберите excel файл', dir=path_dir, filter="Excel Files (*.xls *.xlsx)")
        if result and result[0]:
            self.company.int_file_path = result[0]
            self.ui.select_path_excel_value.setText(result[0])

    def open_select_path_csv(self):
        if self.company.int_file_path:
            path_dir = os.path.dirname(self.company.int_file_path)
        else:
            path_dir = None
        result = QFileDialog.getOpenFileName(self, 'Выберите csv файл', dir=path_dir, filter="CSV File (*.csv)")
        if result and result[0]:
            self.company.int_file_path = result[0]
            self.ui.select_path_csv_value.setText(result[0])
