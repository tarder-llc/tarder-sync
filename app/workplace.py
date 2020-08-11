from datetime import datetime, timedelta

from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal, QObject, QTimer, QEventLoop

from app.shared.api_service import ApiService
from app.shared.constants import Constants
from app.shared.helpers import Helpers, obj
from app.shared.storage_service import StorageService
from app.shared.text_logger import TextLogger
from app.worker import Worker


class WorkPlace(QObject):
    is_active = False

    on_update = Signal(list)
    
    def __init__(self, parent):
        super().__init__()

        self.on_update.connect(parent.on_update)

        self.logging = TextLogger().log

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.work)
        self.timer.start(1 * 1000)

    def stop(self):
        self.is_active = False
        self.timer.stop()
        self.on_update.disconnect()

    def pause(self):
        self.is_active = False

    def start(self, timeout_seconds=None):
        if timeout_seconds:
            QTimer().singleShot(timeout_seconds * 1000, lambda: self.start())
        else:
            self.is_active = True

    def work(self):
        if not self.is_active:
            return

        refresh_companies_result = self.check_refresh_companies()
        if refresh_companies_result == False:
            self.log('Синхронизация выключена до следующего успешного обновления организаций с сервера', True)
            return

        companies = StorageService().get_companies()
        self.on_update.emit(obj({'companies': companies}))

        for company in companies:
            Worker(self, company).work()

        pass

    def log(self, text, is_error=False, is_success=False):

        if is_error:
            self.logging.error(text)
        elif is_success:
            self.logging.log(Constants.LOG_GOOD, text)
        else:
            self.logging.info(text)

    def check_refresh_companies(self):
        companies_next = Helpers.parse_date(StorageService().get_value('sync_companies_next'))

        result = obj({'status': None})  # None - if not changed

        if not companies_next or Helpers.now() > companies_next:
            try:
                wait_loop = QEventLoop()

                self.log('Начинаю загрузку компаний с сервера Tarder')

                def on_success(array):
                    self.log('Загрузка компаний успешно завершена', is_success=True)
                    result.status = True
                    wait_loop.exit()

                def on_error(text=None):
                    result.status = False
                    wait_loop.exit()

                self.refresh_companies(on_success, on_error)

                wait_loop.exec_()
            except Exception as error:
                self.log('Задача завершена с ошибкой: {}'.format(error), is_error=True)
                StorageService().set_value('sync_companies_last_error', str(Helpers.now()))
                result.status = False

        if result.status == False:
            StorageService().set_value('sync_companies_next',
                                       str(Helpers.now() + timedelta(seconds=Constants.PERIOD_COMPANIES_ERROR)))
            self.on_update.emit(obj())
        elif result.status == True:
            StorageService().set_value('sync_companies_next',
                                       str(Helpers.now() + timedelta(seconds=Constants.PERIOD_COMPANIES)))
            self.on_update.emit(obj())


        return result.status

    def refresh_companies(self, on_success=lambda x: x, on_error=lambda x: x):
        self.log('Обновляю компании...')
        StorageService().set_value('sync_companies_now', True)
        self.on_update.emit(obj())

        def on_success_int(result):
            if result.companies:
                StorageService().upsert_companies(result.companies)
                companies = StorageService().get_companies()
                # set default variables
                self.log('Получено компаний: ' + str(len(companies)))
                StorageService().set_value('sync_companies_last', str(Helpers.now()))
                StorageService().set_value('sync_companies_now', False)
                self.on_update.emit(obj({'companies': companies}))
                on_success(companies)
            else:
                error = 'Ошибка получения компаний: пустой ответ от сервера'
                self.log(error, is_error=True)
                StorageService().set_value('sync_companies_last_error', str(Helpers.now()))
                StorageService().set_value('sync_companies_now', False)
                self.on_update.emit(obj())
                on_error(error)
            pass

        def on_error_int(error):
            self.log('Ошибка: ' + str(error), True)
            StorageService().set_value('sync_companies_last_error', str(Helpers.now()))
            StorageService().set_value('sync_companies_now', False)
            self.on_update.emit(obj())
            on_error(error)
            pass

        ApiService().get_companies({}, on_success_int, on_error_int)


class WorkPlaceThread(QThread, WorkPlace):
    on_update = Signal(object)

    def run(self):
        self.on_signal.emit('TEST')
