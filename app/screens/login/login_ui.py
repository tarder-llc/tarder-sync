# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Form.resize(722, 260)
        Form.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.wrapper = QWidget(Form)
        self.wrapper.setObjectName(u"wrapper")
        self.wrapper.setStyleSheet(u"#wrapper{\n"
" background: white\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.wrapper)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 1, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.wrapper)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 36))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")
        self.label_5.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.api_key_value = QLineEdit(self.wrapper)
        self.api_key_value.setObjectName(u"api_key_value")
        self.api_key_value.setMinimumSize(QSize(0, 30))
        self.api_key_value.setFont(font)
        self.api_key_value.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.api_key_value)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.api_key_login_b = QPushButton(self.wrapper)
        self.api_key_login_b.setObjectName(u"api_key_login_b")
        self.api_key_login_b.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.api_key_login_b.sizePolicy().hasHeightForWidth())
        self.api_key_login_b.setSizePolicy(sizePolicy)
        self.api_key_login_b.setMinimumSize(QSize(0, 30))
        self.api_key_login_b.setBaseSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.api_key_login_b)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.api_key_message = QLabel(self.wrapper)
        self.api_key_message.setObjectName(u"api_key_message")
        self.api_key_message.setEnabled(True)

        self.verticalLayout_5.addWidget(self.api_key_message)

        self.label_4 = QLabel(self.wrapper)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 36))

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.wrapper)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.login_value = QLineEdit(self.wrapper)
        self.login_value.setObjectName(u"login_value")
        self.login_value.setMinimumSize(QSize(0, 30))
        self.login_value.setFont(font)
        self.login_value.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.login_value)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.wrapper)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.password_value = QLineEdit(self.wrapper)
        self.password_value.setObjectName(u"password_value")
        self.password_value.setMinimumSize(QSize(0, 30))
        self.password_value.setFont(font)
        self.password_value.setStyleSheet(u"")
        self.password_value.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_value)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.login_b = QPushButton(self.wrapper)
        self.login_b.setObjectName(u"login_b")
        sizePolicy.setHeightForWidth(self.login_b.sizePolicy().hasHeightForWidth())
        self.login_b.setSizePolicy(sizePolicy)
        self.login_b.setMinimumSize(QSize(0, 30))
        self.login_b.setBaseSize(QSize(0, 0))
        self.login_b.setStyleSheet(u"padding: 0 20px")

        self.verticalLayout_3.addWidget(self.login_b)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.login_message = QLabel(self.wrapper)
        self.login_message.setObjectName(u"login_message")
        self.login_message.setEnabled(True)

        self.verticalLayout_5.addWidget(self.login_message)


        self.verticalLayout_6.addWidget(self.wrapper)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Api \u043a\u043b\u044e\u0447</span> \u0434\u043b\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440, \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435: <a href=\"https://tarder.ru/info/business/avtomaticheskoe-obnovlenie-dannyh\"><span style=\" text-decoration: underline; color:#0000ff;\">tarder info</span></a></p></body></html>", None))
        self.api_key_value.setText("")
        self.api_key_login_b.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.api_key_message.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u0418\u043b\u0438 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0435 \u0435\u0433\u043e, \u0443\u043a\u0430\u0437\u0430\u0432 \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c </span><span style=\" font-size:10pt; font-weight:600;\">\u0441\u0443\u043f\u0435\u0440 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Email", None))
        self.login_value.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_value.setText("")
        self.login_b.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043a\u043b\u044e\u0447", None))
        self.login_message.setText("")
    # retranslateUi

