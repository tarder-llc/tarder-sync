# -*- coding: utf8 -*-
import locale
import os
import sys
from pathlib import Path

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QEvent
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMessageBox, QCheckBox

from app.screens.general.general import GeneralScreen
from app.screens.login.login import LoginScreen
from app.shared.main_service import MainService
from app.shared.storage_service import StorageService

QWIDGET_SIZE_MAX = 16777215
MAX_GET_ENT = 1000

import assets_rc

class MainWindow(QMainWindow):
    selectedScreen = 'login'

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.init()

    def init(self):
        MainService().main = self
        self.setWindowTitle('Tarder Sync')
        # self.setWindowFlag(QtCore.Qt.CustomizeWindowHint, True)
        # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        if MainService().isLogin:
            self.selectedScreen = 'general'
        else:
            self.selectedScreen = 'login'

        # init language
        translator = QtCore.QTranslator(app)
        locale = QtCore.QLocale.system().name()
        path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
        translator.load('qt_%s' % locale, path)
        app.installTranslator(translator)

        # init tray icon
        self.tray_icon = QSystemTrayIcon(QIcon(':/assets/logo_blue_254.png'), self.parent)
        self.setWindowIcon(QIcon(':/assets/logo_blue_254.png'))
        # Restore the window when the tray icon is double clicked.
        self.tray_icon.activated.connect(self.restore_window)
        self.tray_icon.show()

        # menu on tray
        menu = QtWidgets.QMenu(self)
        menu.addAction("Открыть основное окно").triggered.connect(lambda x: self.show_and_activate_window())
        # menu.addAction("Остановить синхронизхацию")
        menu.addAction("Выйти").triggered.connect(self.exit)
        self.tray_icon.setContextMenu(menu)
        # menu.triggered.connect(self.exit)

        self.on_change_screen()

    def event(self, event):

        if event.type() == QEvent.WindowStateChange:
            self.save_settings()

        if (event.type() == QEvent.WindowStateChange and
                self.isMinimized()):

            self.save_settings()
            # The window is already minimized at this point.  AFAIK,
            # there is no hook stop a minimize event. Instead,
            # removing the Qt.Tool flag should remove the window
            # from the taskbar.
            # self.setWindowFlags(self.windowFlags() and ~Qt.Tool)
            self.hide()
            return True
        else:
            return super(MainWindow, self).event(event)

    def exit(self):
        self.save_settings()
        QtCore.QCoreApplication.exit()

    def restore_window(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            # self.tray_icon.hide()
            # self.showNormal will restore the window even if it was
            # minimized.
            # self.showNormal()
            self.show_and_activate_window()

    def show_and_activate_window(self):
        self.showNormal()
        self.raise_()  # for MacOS
        self.activateWindow()  # for Windows
        self.restore_settings()

    def on_change_screen(self):

        if self.selectedScreen == 'general':
            screen = GeneralScreen(self)
            self.setCentralWidget(screen)
            self.setMinimumSize(0, 0)
            self.setMaximumSize(QWIDGET_SIZE_MAX, QWIDGET_SIZE_MAX)
            self.resize(screen.ui.wrapper.sizeHint())
            # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
            # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
            # self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))
        else:
            screen = LoginScreen(self)
            self.setCentralWidget(screen)
            # self.resize(screen.ui.sizeHint())
            self.setFixedSize(screen.ui.wrapper.sizeHint())
            # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
            # self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, QSizePolicy.DefaultType))
            # self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
            # self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
            # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
            # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
            # self.showMaximized()

        self.restore_settings()

    def closeEvent(self, event):
        self.save_settings()

        if StorageService().get_value('hide_on_close'):
            self.tray_icon.show()
            self.hide()
            event.ignore()
        else:
            # reply = QMessageBox.question(
            #     self,
            #     'Сообщение', "Свернуть программу в трей, что бы обмен не останавливался?",
            #     QMessageBox.Yes,
            #     QMessageBox.No)

            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Question)
            msg_box.setWindowTitle('Закрыть или свернуть Tarder Sync')
            msg_box.setText("Свернуть программу в трей, что бы обмен не останавливался?")
            msg_box.addButton('Да', QMessageBox.AcceptRole)
            msg_box.addButton('Нет', QMessageBox.RejectRole)
            msg_box.setDefaultButton(QMessageBox.Cancel)
            dont_show_check_box = QCheckBox("Не спрашивать больше")
            dont_show_check_box.blockSignals(True)
            dont_show_check_box.setCheckable(True)
            # msg_box.setCheckBox(dont_show_check_box)
            msg_box.addButton(dont_show_check_box, QMessageBox.ResetRole)
            reply = msg_box.exec_()

            def save_checkbox_state(value):
                if dont_show_check_box.checkState() == Qt.Checked:
                    StorageService().set_value('hide_on_close', value)

            if reply == QMessageBox.AcceptRole:
                self.tray_icon.show()
                self.hide()
                event.ignore()
                save_checkbox_state(False)
            elif reply == QMessageBox.RejectRole:
                save_checkbox_state(True)
                event.accept()
            else:
                event.ignore()

            # QMainWindow.closeEvent(self, event)

    def save_settings(self):
        StorageService().set_value(self.selectedScreen + "/geometry", self.saveGeometry())
        StorageService().set_value(self.selectedScreen + "/windowState", self.saveState())

    def restore_settings(self):
        self.restoreGeometry(StorageService().get_value(self.selectedScreen + "/geometry"))
        self.restoreState(StorageService().get_value(self.selectedScreen + "/myWidget/windowState"))


def init_main():
    locale.setlocale(locale.LC_ALL, '')

    os.chdir(os.path.dirname(sys.argv[0]))
    Path("logs").mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    assets_rc.qInitResources()
    init_main()
    main = MainWindow()
    if '-hide' not in sys.argv:
        main.show()
    sys.exit(app.exec_())
