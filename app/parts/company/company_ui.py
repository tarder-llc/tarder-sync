# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'company.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1128, 704)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.container_top = QHBoxLayout()
        self.container_top.setObjectName(u"container_top")
        self.container_top.setContentsMargins(-1, -1, 18, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.type_source = QComboBox(Form)
        self.type_source.addItem("")
        self.type_source.addItem("")
        self.type_source.setObjectName(u"type_source")
        self.type_source.setMinimumSize(QSize(165, 0))

        self.verticalLayout_4.addWidget(self.type_source)


        self.container_top.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_top.addItem(self.horizontalSpacer)

        self._2 = QVBoxLayout()
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, 10, -1, -1)
        self.undo_changes_b = QPushButton(Form)
        self.undo_changes_b.setObjectName(u"undo_changes_b")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_changes_b.sizePolicy().hasHeightForWidth())
        self.undo_changes_b.setSizePolicy(sizePolicy)
        self.undo_changes_b.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        self.undo_changes_b.setFont(font)
        self.undo_changes_b.setStyleSheet(u"padding: 5px 10px;")

        self._2.addWidget(self.undo_changes_b)


        self.container_top.addLayout(self._2)


        self.horizontalLayout_2.addLayout(self.container_top)

        self._4 = QVBoxLayout()
        self._4.setObjectName(u"_4")
        self._4.setContentsMargins(-1, 10, -1, -1)
        self.toggle_active_worker_b = QPushButton(Form)
        self.toggle_active_worker_b.setObjectName(u"toggle_active_worker_b")
        sizePolicy.setHeightForWidth(self.toggle_active_worker_b.sizePolicy().hasHeightForWidth())
        self.toggle_active_worker_b.setSizePolicy(sizePolicy)
        self.toggle_active_worker_b.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.toggle_active_worker_b.setFont(font1)
        self.toggle_active_worker_b.setStyleSheet(u"padding: 5px 10px; ")
        self.toggle_active_worker_b.setCheckable(True)
        self.toggle_active_worker_b.setChecked(False)
        self.toggle_active_worker_b.setAutoExclusive(False)
        self.toggle_active_worker_b.setFlat(False)

        self._4.addWidget(self.toggle_active_worker_b)


        self.horizontalLayout_2.addLayout(self._4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.container_1c = QGroupBox(Form)
        self.container_1c.setObjectName(u"container_1c")
        self.verticalLayout_3 = QVBoxLayout(self.container_1c)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.container_1c)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_17.addWidget(self.label_14)

        self.con_type = QComboBox(self.container_1c)
        self.con_type.addItem("")
        self.con_type.addItem("")
        self.con_type.setObjectName(u"con_type")
        self.con_type.setMinimumSize(QSize(165, 0))

        self.verticalLayout_17.addWidget(self.con_type)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)

        self.type1c_srv = QWidget(self.container_1c)
        self.type1c_srv.setObjectName(u"type1c_srv")
        self.type1c_srv.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.type1c_srv.sizePolicy().hasHeightForWidth())
        self.type1c_srv.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.type1c_srv)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.type1c_srv)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.label_3)

        self.server_name = QLineEdit(self.type1c_srv)
        self.server_name.setObjectName(u"server_name")

        self.verticalLayout_2.addWidget(self.server_name)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_16 = QLabel(self.type1c_srv)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setScaledContents(False)

        self.verticalLayout_6.addWidget(self.label_16)

        self.base_name = QLineEdit(self.type1c_srv)
        self.base_name.setObjectName(u"base_name")

        self.verticalLayout_6.addWidget(self.base_name)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addWidget(self.type1c_srv)

        self.type1c_file = QWidget(self.container_1c)
        self.type1c_file.setObjectName(u"type1c_file")
        sizePolicy1.setHeightForWidth(self.type1c_file.sizePolicy().hasHeightForWidth())
        self.type1c_file.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.type1c_file)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.type1c_file)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setScaledContents(False)

        self.verticalLayout_15.addWidget(self.label_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.select_path_value = QLineEdit(self.type1c_file)
        self.select_path_value.setObjectName(u"select_path_value")
        self.select_path_value.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.select_path_value)

        self.select_path_b = QPushButton(self.type1c_file)
        self.select_path_b.setObjectName(u"select_path_b")

        self.horizontalLayout_9.addWidget(self.select_path_b)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_11.addLayout(self.verticalLayout_15)


        self.horizontalLayout_5.addWidget(self.type1c_file)

        self.wrapLogin = QVBoxLayout()
        self.wrapLogin.setObjectName(u"wrapLogin")
        self.label_4 = QLabel(self.container_1c)
        self.label_4.setObjectName(u"label_4")

        self.wrapLogin.addWidget(self.label_4)

        self.base_login = QLineEdit(self.container_1c)
        self.base_login.setObjectName(u"base_login")

        self.wrapLogin.addWidget(self.base_login)


        self.horizontalLayout_5.addLayout(self.wrapLogin)

        self.wrapPassword = QVBoxLayout()
        self.wrapPassword.setObjectName(u"wrapPassword")
        self.label_5 = QLabel(self.container_1c)
        self.label_5.setObjectName(u"label_5")

        self.wrapPassword.addWidget(self.label_5)

        self.base_password = QLineEdit(self.container_1c)
        self.base_password.setObjectName(u"base_password")
        self.base_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.base_password.setEchoMode(QLineEdit.Password)

        self.wrapPassword.addWidget(self.base_password)


        self.horizontalLayout_5.addLayout(self.wrapPassword)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.connection_1c_value = QLabel(self.container_1c)
        self.connection_1c_value.setObjectName(u"connection_1c_value")
        self.connection_1c_value.setStyleSheet(u"padding: 0 10px")

        self.horizontalLayout.addWidget(self.connection_1c_value)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.container_1c)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.type_1c = QComboBox(self.container_1c)
        self.type_1c.addItem("")
        self.type_1c.setObjectName(u"type_1c")
        self.type_1c.setMinimumSize(QSize(165, 0))

        self.horizontalLayout_7.addWidget(self.type_1c)


        self.horizontalLayout.addLayout(self.horizontalLayout_7)

        self.connect_to_1c_b = QPushButton(self.container_1c)
        self.connect_to_1c_b.setObjectName(u"connect_to_1c_b")
        sizePolicy.setHeightForWidth(self.connect_to_1c_b.sizePolicy().hasHeightForWidth())
        self.connect_to_1c_b.setSizePolicy(sizePolicy)
        self.connect_to_1c_b.setMinimumSize(QSize(0, 30))
        self.connect_to_1c_b.setFont(font1)
        self.connect_to_1c_b.setStyleSheet(u"padding: 5px 10px; ")
        self.connect_to_1c_b.setCheckable(True)
        self.connect_to_1c_b.setChecked(False)
        self.connect_to_1c_b.setAutoExclusive(False)
        self.connect_to_1c_b.setFlat(False)

        self.horizontalLayout.addWidget(self.connect_to_1c_b)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.container_1c)

        self.container_excel = QGroupBox(Form)
        self.container_excel.setObjectName(u"container_excel")
        self.verticalLayout_11 = QVBoxLayout(self.container_excel)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 9, 9, -1)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.aaaaa_file_3 = QWidget(self.container_excel)
        self.aaaaa_file_3.setObjectName(u"aaaaa_file_3")
        sizePolicy1.setHeightForWidth(self.aaaaa_file_3.sizePolicy().hasHeightForWidth())
        self.aaaaa_file_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_17 = QHBoxLayout(self.aaaaa_file_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_22 = QLabel(self.aaaaa_file_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setScaledContents(False)

        self.verticalLayout_20.addWidget(self.label_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.select_path_excel_value = QLineEdit(self.aaaaa_file_3)
        self.select_path_excel_value.setObjectName(u"select_path_excel_value")
        self.select_path_excel_value.setEnabled(False)

        self.horizontalLayout_18.addWidget(self.select_path_excel_value)

        self.select_path_excel_b = QPushButton(self.aaaaa_file_3)
        self.select_path_excel_b.setObjectName(u"select_path_excel_b")

        self.horizontalLayout_18.addWidget(self.select_path_excel_b)


        self.verticalLayout_20.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_17.addLayout(self.verticalLayout_20)


        self.horizontalLayout_15.addWidget(self.aaaaa_file_3)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 20, 0, -1)
        self.connect_to_xls_b = QPushButton(self.container_excel)
        self.connect_to_xls_b.setObjectName(u"connect_to_xls_b")
        sizePolicy.setHeightForWidth(self.connect_to_xls_b.sizePolicy().hasHeightForWidth())
        self.connect_to_xls_b.setSizePolicy(sizePolicy)
        self.connect_to_xls_b.setMinimumSize(QSize(0, 30))
        self.connect_to_xls_b.setFont(font1)
        self.connect_to_xls_b.setStyleSheet(u"padding: 5px 10px; ")
        self.connect_to_xls_b.setCheckable(True)
        self.connect_to_xls_b.setChecked(False)
        self.connect_to_xls_b.setAutoExclusive(False)
        self.connect_to_xls_b.setFlat(False)

        self.verticalLayout_19.addWidget(self.connect_to_xls_b)


        self.horizontalLayout_15.addLayout(self.verticalLayout_19)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addWidget(self.container_excel)

        self.container_csv = QGroupBox(Form)
        self.container_csv.setObjectName(u"container_csv")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.container_csv.sizePolicy().hasHeightForWidth())
        self.container_csv.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.container_csv)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 9, 9, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.aaaaa_file_4 = QWidget(self.container_csv)
        self.aaaaa_file_4.setObjectName(u"aaaaa_file_4")
        sizePolicy1.setHeightForWidth(self.aaaaa_file_4.sizePolicy().hasHeightForWidth())
        self.aaaaa_file_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_19 = QHBoxLayout(self.aaaaa_file_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_23 = QLabel(self.aaaaa_file_4)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)
        self.label_23.setScaledContents(False)

        self.verticalLayout_21.addWidget(self.label_23)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.select_path_csv_value = QLineEdit(self.aaaaa_file_4)
        self.select_path_csv_value.setObjectName(u"select_path_csv_value")
        self.select_path_csv_value.setEnabled(False)

        self.horizontalLayout_20.addWidget(self.select_path_csv_value)

        self.select_path_csv_b = QPushButton(self.aaaaa_file_4)
        self.select_path_csv_b.setObjectName(u"select_path_csv_b")

        self.horizontalLayout_20.addWidget(self.select_path_csv_b)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_19.addLayout(self.verticalLayout_21)


        self.horizontalLayout_16.addWidget(self.aaaaa_file_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 20, 0, -1)
        self.connect_to_csv_b = QPushButton(self.container_csv)
        self.connect_to_csv_b.setObjectName(u"connect_to_csv_b")
        sizePolicy.setHeightForWidth(self.connect_to_csv_b.sizePolicy().hasHeightForWidth())
        self.connect_to_csv_b.setSizePolicy(sizePolicy)
        self.connect_to_csv_b.setMinimumSize(QSize(0, 30))
        self.connect_to_csv_b.setFont(font1)
        self.connect_to_csv_b.setStyleSheet(u"padding: 5px 10px; ")
        self.connect_to_csv_b.setCheckable(True)
        self.connect_to_csv_b.setChecked(False)
        self.connect_to_csv_b.setAutoExclusive(False)
        self.connect_to_csv_b.setFlat(False)

        self.verticalLayout_22.addWidget(self.connect_to_csv_b)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addWidget(self.container_csv)

        self.container_control = QGroupBox(Form)
        self.container_control.setObjectName(u"container_control")
        self.verticalLayout_13 = QVBoxLayout(self.container_control)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.container_control)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.company_inn_value = QLabel(self.container_control)
        self.company_inn_value.setObjectName(u"company_inn_value")
        sizePolicy4.setHeightForWidth(self.company_inn_value.sizePolicy().hasHeightForWidth())
        self.company_inn_value.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.company_inn_value)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.company_name_value = QLabel(self.container_control)
        self.company_name_value.setObjectName(u"company_name_value")
        sizePolicy4.setHeightForWidth(self.company_name_value.sizePolicy().hasHeightForWidth())
        self.company_name_value.setSizePolicy(sizePolicy4)
        self.company_name_value.setLayoutDirection(Qt.LeftToRight)
        self.company_name_value.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.company_name_value)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.find_company_b = QPushButton(self.container_control)
        self.find_company_b.setObjectName(u"find_company_b")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.find_company_b.sizePolicy().hasHeightForWidth())
        self.find_company_b.setSizePolicy(sizePolicy5)
        self.find_company_b.setFont(font1)
        self.find_company_b.setStyleSheet(u"padding: 5px 10px;")

        self.horizontalLayout_3.addWidget(self.find_company_b)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.sync_all_b = QPushButton(self.container_control)
        self.sync_all_b.setObjectName(u"sync_all_b")
        sizePolicy5.setHeightForWidth(self.sync_all_b.sizePolicy().hasHeightForWidth())
        self.sync_all_b.setSizePolicy(sizePolicy5)
        self.sync_all_b.setFont(font1)
        self.sync_all_b.setStyleSheet(u"padding: 5px 10px;")

        self.horizontalLayout_6.addWidget(self.sync_all_b)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.container_control)

        self.company_tabs = QTabWidget(Form)
        self.company_tabs.setObjectName(u"company_tabs")
        self.log_tab = QWidget()
        self.log_tab.setObjectName(u"log_tab")
        self.verticalLayout_5 = QVBoxLayout(self.log_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.log_text = QTextEdit(self.log_tab)
        self.log_text.setObjectName(u"log_text")

        self.verticalLayout_5.addWidget(self.log_text)

        self.company_tabs.addTab(self.log_tab, "")
        self.items_tab = QWidget()
        self.items_tab.setObjectName(u"items_tab")
        self.verticalLayout_14 = QVBoxLayout(self.items_tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.container_control_items = QHBoxLayout()
        self.container_control_items.setObjectName(u"container_control_items")
        self.container_control_items.setContentsMargins(-1, 0, -1, -1)
        self.label_11 = QLabel(self.items_tab)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_11.setFont(font2)

        self.container_control_items.addWidget(self.label_11)

        self.sync_with_tarder_items_b = QPushButton(self.items_tab)
        self.sync_with_tarder_items_b.setObjectName(u"sync_with_tarder_items_b")
        sizePolicy5.setHeightForWidth(self.sync_with_tarder_items_b.sizePolicy().hasHeightForWidth())
        self.sync_with_tarder_items_b.setSizePolicy(sizePolicy5)
        self.sync_with_tarder_items_b.setFont(font1)
        self.sync_with_tarder_items_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_items.addWidget(self.sync_with_tarder_items_b)

        self.sync_with_source_items_b = QPushButton(self.items_tab)
        self.sync_with_source_items_b.setObjectName(u"sync_with_source_items_b")
        sizePolicy5.setHeightForWidth(self.sync_with_source_items_b.sizePolicy().hasHeightForWidth())
        self.sync_with_source_items_b.setSizePolicy(sizePolicy5)
        self.sync_with_source_items_b.setFont(font1)
        self.sync_with_source_items_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_items.addWidget(self.sync_with_source_items_b)


        self.verticalLayout_14.addLayout(self.container_control_items)

        self.items_table = QTableWidget(self.items_tab)
        if (self.items_table.columnCount() < 6):
            self.items_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.items_table.setObjectName(u"items_table")
        self.items_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_14.addWidget(self.items_table)

        self.company_tabs.addTab(self.items_tab, "")
        self.points_tab = QWidget()
        self.points_tab.setObjectName(u"points_tab")
        self.verticalLayout_8 = QVBoxLayout(self.points_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.container_control_points = QHBoxLayout()
        self.container_control_points.setObjectName(u"container_control_points")
        self.container_control_points.setContentsMargins(-1, 0, -1, -1)
        self.label_12 = QLabel(self.points_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.container_control_points.addWidget(self.label_12)

        self.sync_with_tarder_points_b = QPushButton(self.points_tab)
        self.sync_with_tarder_points_b.setObjectName(u"sync_with_tarder_points_b")
        sizePolicy5.setHeightForWidth(self.sync_with_tarder_points_b.sizePolicy().hasHeightForWidth())
        self.sync_with_tarder_points_b.setSizePolicy(sizePolicy5)
        self.sync_with_tarder_points_b.setFont(font1)
        self.sync_with_tarder_points_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_points.addWidget(self.sync_with_tarder_points_b)

        self.sync_with_source_points_b = QPushButton(self.points_tab)
        self.sync_with_source_points_b.setObjectName(u"sync_with_source_points_b")
        sizePolicy5.setHeightForWidth(self.sync_with_source_points_b.sizePolicy().hasHeightForWidth())
        self.sync_with_source_points_b.setSizePolicy(sizePolicy5)
        self.sync_with_source_points_b.setFont(font1)
        self.sync_with_source_points_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_points.addWidget(self.sync_with_source_points_b)


        self.verticalLayout_8.addLayout(self.container_control_points)

        self.points_table = QTableWidget(self.points_tab)
        if (self.points_table.columnCount() < 5):
            self.points_table.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.points_table.setObjectName(u"points_table")
        self.points_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_8.addWidget(self.points_table)

        self.company_tabs.addTab(self.points_tab, "")
        self.item_in_points_tab = QWidget()
        self.item_in_points_tab.setObjectName(u"item_in_points_tab")
        self.verticalLayout_9 = QVBoxLayout(self.item_in_points_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.container_control_iip = QHBoxLayout()
        self.container_control_iip.setObjectName(u"container_control_iip")
        self.container_control_iip.setContentsMargins(-1, 0, -1, -1)
        self.label_13 = QLabel(self.item_in_points_tab)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font2)

        self.container_control_iip.addWidget(self.label_13)

        self.container_type_of_price = QWidget(self.item_in_points_tab)
        self.container_type_of_price.setObjectName(u"container_type_of_price")
        sizePolicy3.setHeightForWidth(self.container_type_of_price.sizePolicy().hasHeightForWidth())
        self.container_type_of_price.setSizePolicy(sizePolicy3)
        self._3 = QHBoxLayout(self.container_type_of_price)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.container_type_of_price)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self._3.addWidget(self.label_7)

        self.price_type = QComboBox(self.container_type_of_price)
        self.price_type.setObjectName(u"price_type")
        self.price_type.setMinimumSize(QSize(165, 0))
        self.price_type.setEditable(True)

        self._3.addWidget(self.price_type)


        self.container_control_iip.addWidget(self.container_type_of_price)

        self.sync_with_source_iip_b = QPushButton(self.item_in_points_tab)
        self.sync_with_source_iip_b.setObjectName(u"sync_with_source_iip_b")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sync_with_source_iip_b.sizePolicy().hasHeightForWidth())
        self.sync_with_source_iip_b.setSizePolicy(sizePolicy6)
        self.sync_with_source_iip_b.setFont(font1)
        self.sync_with_source_iip_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_iip.addWidget(self.sync_with_source_iip_b)

        self.upload_to_tarder_iip_b = QPushButton(self.item_in_points_tab)
        self.upload_to_tarder_iip_b.setObjectName(u"upload_to_tarder_iip_b")
        sizePolicy6.setHeightForWidth(self.upload_to_tarder_iip_b.sizePolicy().hasHeightForWidth())
        self.upload_to_tarder_iip_b.setSizePolicy(sizePolicy6)
        self.upload_to_tarder_iip_b.setFont(font1)
        self.upload_to_tarder_iip_b.setStyleSheet(u"padding: 5px 10px;")

        self.container_control_iip.addWidget(self.upload_to_tarder_iip_b)


        self.verticalLayout_9.addLayout(self.container_control_iip)

        self.item_in_points_table = QTableWidget(self.item_in_points_tab)
        if (self.item_in_points_table.columnCount() < 5):
            self.item_in_points_table.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.item_in_points_table.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.item_in_points_table.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.item_in_points_table.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.item_in_points_table.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.item_in_points_table.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.item_in_points_table.setObjectName(u"item_in_points_table")
        self.item_in_points_table.horizontalHeader().setCascadingSectionResizes(False)
        self.item_in_points_table.horizontalHeader().setDefaultSectionSize(150)
        self.item_in_points_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.item_in_points_table.horizontalHeader().setStretchLastSection(False)
        self.item_in_points_table.verticalHeader().setVisible(False)
        self.item_in_points_table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_9.addWidget(self.item_in_points_table)

        self.company_tabs.addTab(self.item_in_points_tab, "")

        self.verticalLayout.addWidget(self.company_tabs)


        self.retranslateUi(Form)

        self.toggle_active_worker_b.setDefault(False)
        self.connect_to_1c_b.setDefault(False)
        self.connect_to_xls_b.setDefault(False)
        self.connect_to_csv_b.setDefault(False)
        self.company_tabs.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.type_source.setItemText(0, QCoreApplication.translate("Form", u"1\u0441 \u041f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.type_source.setItemText(1, QCoreApplication.translate("Form", u"Excel \u0444\u0430\u0439\u043b", None))

        self.undo_changes_b.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.toggle_active_worker_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u043e\u0431\u043c\u0435\u043d", None))
        self.container_1c.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.con_type.setItemText(0, QCoreApplication.translate("Form", u"\u0424\u0430\u0439\u043b\u043e\u0432\u0430\u044f", None))
        self.con_type.setItemText(1, QCoreApplication.translate("Form", u"\u0421\u0435\u0440\u0432\u0435\u0440\u043d\u0430\u044f", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0431\u0430\u0437\u0435", None))
        self.select_path_value.setText("")
        self.select_path_b.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.base_login.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c (\u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c)", None))
        self.connection_1c_value.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u0431\u0430\u0437\u044b", None))
        self.type_1c.setItemText(0, QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))

        self.connect_to_1c_b.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0431\u0430\u0437\u0435", None))
        self.container_excel.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0444\u0430\u0439\u043b\u0443 Excel", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.select_path_excel_value.setText(QCoreApplication.translate("Form", u"G:/BASE/1c/DemoRetailBase", None))
        self.select_path_excel_b.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.connect_to_xls_b.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.container_csv.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0444\u0430\u0439\u043b\u0443 CSV", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.select_path_csv_value.setText(QCoreApplication.translate("Form", u"G:/BASE/1c/DemoRetailBase", None))
        self.select_path_csv_b.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.connect_to_csv_b.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.container_control.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u043d \u0432 Tarder:", None))
        self.company_inn_value.setText(QCoreApplication.translate("Form", u"\u043d\u0435 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d", None))
        self.company_name_value.setText(QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0439\u0442\u0438 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044e \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.find_company_b.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044e \u0432 \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0435", None))
#if QT_CONFIG(tooltip)
        self.sync_all_b.setToolTip(QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0440\u0443\u0447\u043d\u0443\u044e. \u041d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 - \u0432\u043c\u0435\u0441\u0442\u043e \u044d\u0442\u043e\u0433\u043e \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u0430\u0432\u0442\u043e\u043e\u0431\u043c\u0435\u043d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.sync_all_b.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.sync_all_b.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.sync_all_b.setText(QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0451", None))
#if QT_CONFIG(shortcut)
        self.sync_all_b.setShortcut(QCoreApplication.translate("Form", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.company_tabs.setTabText(self.company_tabs.indexOf(self.log_tab), QCoreApplication.translate("Form", u"\u041b\u043e\u0433", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.sync_with_tarder_items_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 Tarder", None))
        self.sync_with_source_items_b.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u0435\u0440\u0438\u0442\u044c c \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u043e\u043c", None))
        ___qtablewidgetitem = self.items_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Tarder", None));
        ___qtablewidgetitem1 = self.items_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f Tarder", None));
        ___qtablewidgetitem2 = self.items_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"SKU Tarder", None));
        ___qtablewidgetitem3 = self.items_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"ID \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 Tarder", None));
        ___qtablewidgetitem4 = self.items_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ID \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        ___qtablewidgetitem5 = self.items_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        self.company_tabs.setTabText(self.company_tabs.indexOf(self.items_tab), QCoreApplication.translate("Form", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u0435\u043a \u043f\u0440\u043e\u0434\u0430\u0436 ", None))
        self.sync_with_tarder_points_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 Tarder", None))
        self.sync_with_source_points_b.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u0435\u0440\u0438\u0442\u044c c \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u043e\u043c", None))
        ___qtablewidgetitem6 = self.points_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"ID Tarder", None));
        ___qtablewidgetitem7 = self.points_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f Tarder", None));
        ___qtablewidgetitem8 = self.points_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"ID \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 Tarder", None));
        ___qtablewidgetitem9 = self.points_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"ID \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        ___qtablewidgetitem10 = self.points_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        self.company_tabs.setTabText(self.company_tabs.indexOf(self.points_tab), QCoreApplication.translate("Form", u"\u0422\u043e\u0447\u043a\u0438 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0446\u0435\u043d \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0446\u0435\u043d:", None))
        self.sync_with_source_iip_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None))
        self.upload_to_tarder_iip_b.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 Tarder", None))
        ___qtablewidgetitem11 = self.item_in_points_table.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"ID Tarder", None));
        ___qtablewidgetitem12 = self.item_in_points_table.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f Tarder", None));
        ___qtablewidgetitem13 = self.item_in_points_table.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"ID \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 Tarder", None));
        ___qtablewidgetitem14 = self.item_in_points_table.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"ID \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        ___qtablewidgetitem15 = self.item_in_points_table.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None));
        self.company_tabs.setTabText(self.company_tabs.indexOf(self.item_in_points_tab), QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u044b \u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
    # retranslateUi

