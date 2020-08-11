
class Variables(object):

    isDebug = False

    url = ''
    url_api = ''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Variables, cls).__new__(cls)
            cls.instance.on_init()
        return cls.instance

    def on_init(self):
        if self.isDebug:
            self.url = "http://localhost:3000/"
        else:
            self.url = "https://tarder.ru/"

        self.url_api = self.url + "api/"
