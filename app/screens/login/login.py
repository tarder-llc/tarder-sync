from PySide2.QtWidgets import QWidget

from app.screens.login.login_ui import Ui_Form
from app.shared.api_service import ApiService
from app.shared.helpers import Helpers
from app.shared.main_service import MainService
from app.shared.variables import Variables


class LoginScreen(QWidget):

    parent = None

    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        if Variables().isDebug:
            Helpers.set_ui(self, __file__)  # just set ui file
        else:
            self.ui = Ui_Form()
            self.ui.setupUi(self)  # load class from converted ui file

        self.init()
        self.parent = parent

    def init(self):

        self.ui.api_key_value.textChanged[str].connect(self.on_api_key_changed)
        self.ui.api_key_login_b.clicked.connect(self.login)
        self.ui.api_key_message.hide()

        self.ui.login_b.clicked.connect(self.get_api_key)
        self.ui.login_message.hide()

        if ApiService().api_key:
            self.ui.api_key_value.setText(ApiService().api_key)
            self.ui.api_key_login_b.setDisabled(False)
        else:
            self.ui.api_key_value.setText('')
            self.ui.api_key_login_b.setDisabled(True)


    def on_api_key_changed(self, value):
        self.ui.api_key_login_b.setDisabled(not len(value) == 64)

    def get_api_key(self):
        self.ui.login_message.show()
        email = str(self.ui.login_value.text())
        password = str(self.ui.password_value.text())
        if ("@" not in email) or (len(email) < 4):
            self.ui.login_message.setText('Email введен некорректно')
            return
        if len(password) < 4:
            self.ui.login_message.setText('Пароль не указан')
            return

        self.ui.login_message.setText('Отправка запроса')

        def on_success(result):
            self.ui.api_key_value.setText(result.id)
            self.ui.api_key_login_b.setDisabled(False)
            self.ui.login_message.setText('Успешно, теперь нажмите войти')
            pass

        def on_error(error):
            self.ui.login_message.setText('Ошибка: ' + str(error))
            pass

        ApiService().get_key({'email': email, 'password': password}, on_success, on_error)

    def login(self):
        self.ui.login_message.hide()
        self.ui.api_key_message.show()
        api_key = str(self.ui.api_key_value.text())
        if not len(api_key) == 64:
            self.ui.api_key_message.setText('Ключ должен быть длиной 64 символа')
            return

        self.ui.api_key_message.setText('Отправка запроса')

        def on_success(result):
            self.ui.api_key_message.hide()
            self.parent.selectedScreen = 'general'
            self.parent.on_change_screen()
            pass

        def on_error(error):
            if 'not found' in str(error):
                self.ui.api_key_message.setText('Ключ не найден, попробуйте получить новый')
            else:
                self.ui.api_key_message.setText('Ошибка: ' + str(error))
            pass

        MainService().login(api_key, on_success, on_error)
