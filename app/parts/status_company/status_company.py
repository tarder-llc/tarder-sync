from datetime import datetime

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QVBoxLayout

from app.parts.status_company.status_company_ui import Ui_Form
from app.shared.constants import Constants
from app.shared.helpers import Helpers, obj
from app.shared.main_service import MainService
from app.shared.storage_service import StorageService
from app.shared.text_logger import TextLogger
from app.shared.variables import Variables


class StatusCompanyComponent(QWidget):
    ui = None

    company = None

    def __init__(self, parent, company):
        super(StatusCompanyComponent, self).__init__(parent)
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
        self.init()

    def init(self):
        self.logging = TextLogger(company=self.company).log
        self.ui.company_status_b.clicked.connect(self.toggle_enable)
        self.ui.sync_main_run_b.clicked.connect(self.run_now)
        self.fill_view()

    def fill_view(self):

        self.ui.company_name_text.setText(self.company.ext_name)

        if not self.company.ext_enable:
            company_status_image = 'stop.png'
            company_status_text = 'автообмен выключен в виртуальном офисе'
            company_status_b_text = 'Остановить'
            company_status_active = False
        elif self.company.int_enable:
            company_status_image = 'start.png'
            company_status_text = 'автообмен активен'
            company_status_b_text = 'Остановить'
            company_status_active = True
        else:
            company_status_image = 'pause.png'
            company_status_b_text = 'Запустить'
            company_status_text = 'автообмен остановлен'
            company_status_active = True

        self.ui.company_status_img.setPixmap(QPixmap(u":/assets/{}".format(company_status_image)))
        self.ui.company_status_text.setText(company_status_text)
        self.ui.company_status_b.setText(company_status_b_text)
        self.ui.company_status_b.setVisible(company_status_active)
        self.ui.wrap_company.setEnabled(company_status_active)

        main_now = self.company.sync_main_now
        main_last = Helpers.parse_date(self.company.sync_main)
        main_last_error = Helpers.parse_date(self.company.sync_main_error)
        main_next = Helpers.parse_date(self.company.sync_main_next)

        if main_last:
            date = Helpers.get_pretty_date(main_last)
        else:
            date = 'не производилась'

        if not main_last and not main_last_error:
            text_last = 'не производилась'
            color = Constants.COLOR_GREY
            image = 'warning.png'
        # if last attempt is error
        elif main_last_error and (not main_last or main_last < main_last_error):
            text_last = Helpers.get_pretty_date(main_last_error)
            color = Constants.COLOR_RED
            image = 'error.png'
        # if last attempt is success
        else:
            text_last = Helpers.get_pretty_date(main_last)
            color = Constants.COLOR_GREY
            image = 'check_green.png'

        if main_now:
            image = 'refresh.png'

        self.ui.sync_main_date.setText(date)
        self.ui.sync_main_last_text.setStyleSheet('color: {}'.format(color))
        self.ui.sync_main_last_date.setStyleSheet('color: {}'.format(color))
        self.ui.sync_main_last_date.setText(text_last)
        self.ui.sync_main_img.setPixmap(QPixmap(u":/assets/{}".format(image)))

        if main_next:
            text_next = Helpers.get_pretty_date(main_next)
        else:
            text_next = 'при запуске'

        self.ui.sync_main_next_date.setText(text_next)

        self.ui.sync_main_run_b.setEnabled(self.company.int_enable and not main_now and True or False)

        # fill steps
        common = obj()
        for name in ['sync_server_items', 'sync_source_items', 'sync_server_points', 'sync_source_points',
                     'sync_source_iip', 'sync_server_iip']:
            self.fill_step(name, common)

        # fill comparison info
        counts = StorageService().get_company_counts(self.company.ext_id)

        # items
        if counts.items and counts.items == counts.items_compared:
            image = 'check_black.png'
        else:
            image = 'warning.png'
        self.ui.found_items_img.setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.found_items_value.setText('{} из {}'.format(counts.items_compared, counts.items))

        # points
        if counts.points and counts.points == counts.points_compared:
            image = 'check_black.png'
        else:
            image = 'warning.png'
        self.ui.found_points_img.setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.found_points_value.setText('{} из {}'.format(counts.points_compared, counts.points))

        # prices
        if counts.price and counts.price == counts.price_founded:
            image = 'check_black.png'
        else:
            image = 'warning.png'
        self.ui.found_price_img.setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.found_price_value.setText('{} из {}'.format(counts.price_founded, counts.price))

        # counts
        if counts.count and counts.count == counts.count_founded:
            image = 'check_black.png'
        else:
            image = 'warning.png'
        self.ui.found_count_img.setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.found_count_value.setText('{} из {}'.format(counts.count_founded, counts.count))

    def fill_step(self, name, common):
        value_now = self.company.__getvalue__(name + '_now')
        value_last = Helpers.parse_date(self.company.__getvalue__(name))
        value_last_error = Helpers.parse_date(self.company.__getvalue__(name + '_error'))

        if value_last:
            date = Helpers.get_pretty_date(value_last)
        else:
            date = 'не производилась'

        if not value_last and not value_last_error:
            date_last = 'не производилась'
            color = Constants.COLOR_GREY
            image = 'warning.png'
            text_image = 'Попытка не производилась'
        # if last attempt is error
        elif value_last_error and (not value_last or value_last < value_last_error):
            date_last = Helpers.get_pretty_date(value_last_error)
            color = Constants.COLOR_RED
            image = 'error.png'
            text_image = 'Последняя попытка {} была неудачной'.format(date_last)
        # if last attempt is success
        else:
            date_last = Helpers.get_pretty_date(value_last)
            color = Constants.COLOR_GREY
            image = 'check_green.png'
            text_image = 'Последняя попытка {} была удачной'.format(date_last)

        if common.previous_now:
            image = 'check_black.png'

        if value_now:
            image = 'refresh.png'
            common.previous_now = True

        self.ui.__getattribute__(name + '_date').setText(date)
        # self.ui.__getattribute__(name + '_text').setStyleSheet('color: {}'.format(color))
        # self.ui.sync_server_items_date.setStyleSheet('color: {}'.format(color))
        self.ui.__getattribute__(name + '_img').setPixmap(QPixmap(u":/assets/{}".format(image)))
        self.ui.__getattribute__(name + '_img').setToolTip(text_image)


    def update_company(self, props):
        self.company = props.company
        self.fill_view()

    def toggle_enable(self):
        if not self.company.int_enable:
            if StorageService().update_company({"ext_id": self.company.ext_id, "int_enable": True}):
                self.company.int_enable = True
                self.log('Автообмен запущен', is_success=True)
            else:
                self.log('Ошибка при запуске автообмена', is_error=True)
            self.fill_view()
        else:
            if StorageService().update_company({"ext_id": self.company.ext_id, "int_enable": False}):
                self.company.int_enable = False
                self.log('Автообмен остановлен', is_success=True)
            else:
                self.log('Ошибка при остановке автообмена', is_error=True)
            self.fill_view()

    def log(self, text, is_error=False, is_success=False):
        text = "[ {} ] {}".format(self.company.ext_name, text)
        if is_error:
            self.logging.error(text)
        elif is_success:
            self.logging.log(Constants.LOG_GOOD, text)
        else:
            self.logging.info(text)
        pass

    def run_now(self):
        if StorageService().update_company({
            "ext_id": self.company.ext_id,
            "sync_main_next": str(Helpers.now())
        }):
            self.company.int_enable = False
            self.log('Синхронизация будет скоро запущена', is_success=True)
        else:
            self.log('Ошибка при запуске синхронизации вручную', is_error=True)

        self.parent.on_update(obj())