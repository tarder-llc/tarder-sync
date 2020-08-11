from PySide2.QtCore import Slot
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QVBoxLayout
from colorlog import logging

from app.parts.company.company import CompanyComponent
from app.parts.status_company.status_company import StatusCompanyComponent
from app.screens.general.general_ui import Ui_Form
from app.shared.api_service import ApiService
from app.shared.constants import Constants
from app.shared.helpers import Helpers, obj
from app.shared.main_service import MainService
from app.shared.storage_service import StorageService
from app.shared.text_logger import TextLogger
from app.shared.variables import Variables
from app.workplace import WorkPlace


class GeneralScreen(QWidget):
    ui = None
    widgets_companies = []
    widgets_status_companies = []

    def __init__(self, parent=None):
        super(GeneralScreen, self).__init__()
        if Variables().isDebug:
            self.ui = Helpers.get_ui(__file__)  # just load ui file
            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.ui)
        else:
            self.ui = Ui_Form()
            self.ui.setupUi(self)  # load class from converted ui file

        self.init()
        self.parent = parent

    def init(self):
        # MainService().log_widget = self.ui.log_text
        # self.ui.update_companies_b.clicked.connect(MainService().refresh_companies)

        self.widgets_companies = []
        self.widgets_status_companies = []

        self.ui.api_key_logout_b.clicked.connect(self.logout)
        self.ui.autoload_b.clicked.connect(self.toggle_autoload)
        self.ui.api_key_value.setText(ApiService().api_key)

        self.ui.splitter.setSizes([400, 200])

        self.clear_tabs()
        self.clear_statuses()

        self.ui.tabs.setCurrentIndex(0)

        # Set up logging
        self.logging = TextLogger(self.ui.log_text).log

        self.workplace = WorkPlace(self)

        def on_success(companies):
            # for company in companies:
            #     self.add_company(company)
            self.workplace.start(10)

        def on_error(error):
            self.on_update(obj())
            self.workplace.start(10)
            pass

        self.workplace.refresh_companies(on_success, on_error)
        self.fill_view()

    def fill_view(self):

        companies_now = StorageService().get_value('sync_companies_now')
        companies_last = Helpers.parse_date(StorageService().get_value('sync_companies_last'))
        companies_last_error = Helpers.parse_date(StorageService().get_value('sync_companies_last_error'))
        companies_next = Helpers.parse_date(StorageService().get_value('sync_companies_next'))

        if companies_last:
            text = Helpers.get_pretty_date(companies_last)
        else:
            text = 'не производилась'
        self.ui.sync_companies_date.setText(text)


        if not companies_last and not companies_last_error:
            text_last = 'не производилась'
            color = Constants.COLOR_GREY
            image = 'warning.png'
        # if last attempt is error
        elif companies_last_error and (not companies_last or companies_last < companies_last_error):
            text_last = Helpers.get_pretty_date(companies_last_error)
            color = Constants.COLOR_RED
            image = 'error.png'
        # if last attempt is success
        else:
            text_last = Helpers.get_pretty_date(companies_last)
            color = Constants.COLOR_GREY
            image = 'check_green.png'

        if companies_now:
            image = 'refresh.png'

        self.ui.sync_companies_last_text.setStyleSheet('color: {}'.format(color))
        self.ui.sync_companies_last_date.setStyleSheet('color: {}'.format(color))
        self.ui.sync_companies_last_date.setText(text_last)
        self.ui.sync_companies_img.setPixmap(QPixmap(u":/assets/{}".format(image)))

        if companies_next:
            text_next = Helpers.get_pretty_date(companies_next)
        else:
            text_next = 'не запланированна'

        self.ui.sync_companies_next_date.setText(text_next)

        # automatic loading at start
        if StorageService().is_in_autoload():
            text = 'Программа в автозагрузке'
            text_b = 'Удалить'
            image = 'check_black.png'
        else:
            text = 'Программы нет в автозагрузке'
            image = 'warning.png'
            text_b = 'Добавить'

        self.ui.autoload_text.setText(text)
        self.ui.autoload_img.setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.autoload_b.setText(text_b)

    def logout(self):
        self.logging.info('Завершаю сеанс обмена')
        self.parent.selectedScreen = 'login'
        StorageService().set_value('api_key', None)
        ApiService().api_key = None
        self.workplace.stop()
        del self.workplace
        del self.logging
        # remove all loggers
        loggers = [logging.getLogger()] + [logging.getLogger(name) for name in logging.root.manager.loggerDict]
        for logger in loggers:
            logger.handlers = []
        self.parent.on_change_screen()

    def clear_tabs(self):
        count = self.ui.tabs.count()
        for i in range(1, count):
            self.ui.tabs.removeTab(1)
        pass

    def clear_statuses(self):
        layout = self.ui.container_companies.layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
        pass

    def add_company_to_tabs(self, company):
        component = CompanyComponent(self, company)
        self.widgets_companies.append(component)
        self.ui.tabs.addTab(component, company.ext_name)
        pass

    def add_company_to_statuses(self, company):
        component = StatusCompanyComponent(self, company)
        self.widgets_status_companies.append(component)
        self.ui.container_companies.layout().addWidget(component)
        pass


    @Slot(object)
    def on_update(self, props):
        if props.companies is None:
            props.companies = StorageService().get_companies()

        for company in props.companies:

            # tab
            for component in self.widgets_companies:
                if component.company.ext_id == company.ext_id:
                    component.update_company(obj({'company': company}))
                    break
            else:
                self.add_company_to_tabs(company)

            # status
            for component in self.widgets_status_companies:
                if component.company.ext_id == company.ext_id:
                    component.update_company(obj({'company': company}))
                    break
            else:
                self.add_company_to_statuses(company)


        self.fill_view()

    def toggle_autoload(self):
        if StorageService().is_in_autoload():
            StorageService().change_to_autoload(remove=True)
        else:
            StorageService().change_to_autoload(add=True)
        self.fill_view()