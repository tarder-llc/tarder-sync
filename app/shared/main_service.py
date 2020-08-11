from app.shared.api_service import ApiService
from app.shared.storage_service import StorageService


class MainService(object):
    main = None

    isLogin = False
    api = None
    storage = None

    log_widget = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MainService, cls).__new__(cls)
            cls.instance.on_init()
        return cls.instance

    def on_init(self):
        # init worker - doing work in the background
        # self.worker = Worker(self)
        # self.thread_pool = QThreadPool()
        # self.thread_pool.start(self.worker)

        self.storage = StorageService()
        self.api = ApiService()
        api_key = self.storage.get_value('api_key')
        if not (api_key is None) and len(api_key) > 0:
            self.isLogin = True
            # self.api.api_key = api_key
            # self.worker.active = True
        else:
            self.isLogin = False
            # self.api.api_key = None

    def login(self, api_key, on_success_in, on_error_in):

        def on_success(result):
            self.api.api_key = api_key
            self.isLogin = True
            self.storage.set_value('api_key', api_key)
            if on_success_in:
                on_success_in(result)
            pass

        def on_error(error):

            if on_error_in:
                on_error_in(error)
            pass

        self.api.login({'apiKey': api_key}, on_success, on_error)

    # def log(self, text, is_error=False, prefix=None):
    #     if not self.log_widget:
    #         print('Error - log_widget not set')
    #         return
    #
    #     if prefix:
    #         text = prefix + ': ' + text
    #
    #     # Helpers.add_to_log(self.log_widget, text, is_error)
    #     if is_error:
    #         logging.error(text)
    #     else:
    #         logging.info(text)
    #     pass


    # def refresh_company_data(self, company, on_success=lambda x: x, on_error=lambda x: x):
    #
    #     logging.info(company.ext_name + ' - обновляю данные: ')
    #     self.refresh_items(company.ext_id,
    #                        on_success,
    #                        on_error)
    #
    #     pass

