import logging
import sys
from logging import handlers

from PySide2 import QtGui
from colorlog import colorlog

from app.shared.constants import Constants
from app.shared.main_service import MainService
from app.shared.variables import Variables


class TextLogger(logging.Handler):
    def __init__(self, widget=None, company=None):
        super(TextLogger, self).__init__()

        self.widget = widget
        self.company = company
        if self.widget:
            self.widget.setReadOnly(True)

        self.logging_init()

    def logging_init(self):

        if not self.company:
            name = 'general'
            name_logger = ''
        else:
            name = self.company.ext_inn
            name_logger = name

        # general setup
        if not logging.getLevelName(Constants.LOG_GOOD) == Constants.LOG_GOOD:
            logging.addLevelName(Constants.LOG_GOOD, 'GOOD')

        log = logging.getLogger(name_logger)
        log.setLevel(logging.INFO)
        self.log = log

        # remove standard handler
        if name == 'general' and len(log.handlers) > 0 and log.handlers[0].name is None:
            log.removeHandler(log.handlers[0])

        # we can call this class twice
        if len(log.handlers) == 0:
            # setup for console
            if not self.company:
                format_console = colorlog.ColoredFormatter("%(log_color)s %(asctime)s - %(levelname)s - %(message)s",
                                                           '%d.%m.%Y %H:%M:%S',
                                                           log_colors={'DEBUG': 'reset', 'INFO': 'reset',
                                                                       'WARNING': 'bold_yellow', 'ERROR': 'bold_red',
                                                                       'CRITICAL': 'bold_red', 'GOOD': 'green'}
                                                           )
                handler_console = logging.StreamHandler(sys.stdout)
                handler_console.setFormatter(format_console)
                handler_console.setLevel(logging.DEBUG)
                handler_console.name = 'custom'
                log.addHandler(handler_console)

            # setup for file
            format_file = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", '%d.%m.%Y %H:%M:%S')
            handler_file = handlers.RotatingFileHandler('logs/{}.log'.format(name), maxBytes=(1048576 * 5),
                                                        backupCount=3, encoding='utf-8')
            handler_file.setFormatter(format_file)
            if Variables().isDebug:
                handler_file.setLevel(logging.DEBUG)
            else:
                handler_file.setLevel(logging.INFO)

            handler_file.name = 'custom'
            log.addHandler(handler_file)

        # setup for text widget
        if self.widget:
            format_widget = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", '%d.%m.%Y %H:%M:%S')
            self.setFormatter(format_widget)
            if Variables().isDebug:
                self.setLevel(logging.DEBUG)
            else:
                self.setLevel(logging.INFO)
            log.addHandler(self)

            self.reload_from_file()

        pass

    def emit(self, record):
        if self.widget:
            msg = self.format(record)
            self.widget.append(self.get_html_text(msg))
            self.widget.moveCursor(QtGui.QTextCursor.End)

    def get_html_text(self, text):
        text_to_remove = None
        if ' - WARNING -' in text:
            text_to_remove = ' - WARNING -'
            text = '<font color="{}">{}</font>'.format(Constants.COLOR_RED_LIGHT, text)
        elif ' - ERROR -' in text:
            text_to_remove = ' - ERROR -'
            text = '<font color="{}">{}</font><font color="#000"> </font>'.format(Constants.COLOR_RED, text)
        elif ' - GOOD -' in text:
            text_to_remove = ' - GOOD -'
            text = '<font color="{}">{}</font><font color="#000"> </font>'.format(Constants.COLOR_GREEN, text)
        elif ' - INFO -' in text:
            text_to_remove = ' - INFO -'
            text = '<font color="#000">{}</font>'.format(text)
        elif ' - DEBUG -' in text:
            text_to_remove = ' - DEBUG -'
            text = '<font color="#000">{}</font>'.format(text)
        else:
            text = '<font color="#000">{}</font>'.format(text)

        if text_to_remove:
            t_start = text.find(text_to_remove)
            if t_start >= 0:
                text = text[:t_start] + text[t_start + len(text_to_remove):]

        if self.company:
            t_start = text.find('[ ')
            t_end = text.find(' ] ')
            if t_start >= 0:
                text = text[:t_start] + text[t_end + 3:]
        return text

    def reload_from_file(self):
        if not self.widget:
            return

        if not self.company:
            name = 'general'
        else:
            name = self.company.ext_inn
        file = 'logs/{}.log'.format(name)

        with open(file, mode='r', encoding='utf-8') as f:
            for line in f:
                self.widget.append(self.get_html_text(line))

        self.widget.moveCursor(QtGui.QTextCursor.End)

    def write(self, m):
        pass
