# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_company.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QFont,
                           QPixmap)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1207, 656)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"#Form{\n"
" background: white\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wrapper = QFrame(Form)
        self.wrapper.setObjectName(u"wrapper")
        self.wrapper.setStyleSheet(u"#wrapper{\n"
" background: white\n"
"}")
        self.wrapper.setFrameShape(QFrame.StyledPanel)
        self.wrapper.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.wrapper)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.wrap_top = QWidget(self.wrapper)
        self.wrap_top.setObjectName(u"wrap_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wrap_top.sizePolicy().hasHeightForWidth())
        self.wrap_top.setSizePolicy(sizePolicy1)
        self.wrap_top.setMinimumSize(QSize(0, 0))
        self.wrap_top.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.wrap_top)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 6, 0, 6)
        self.company_status_img = QLabel(self.wrap_top)
        self.company_status_img.setObjectName(u"company_status_img")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.company_status_img.sizePolicy().hasHeightForWidth())
        self.company_status_img.setSizePolicy(sizePolicy2)
        self.company_status_img.setMinimumSize(QSize(20, 20))
        self.company_status_img.setMaximumSize(QSize(20, 20))
        self.company_status_img.setPixmap(QPixmap(u":/assets/start.png"))
        self.company_status_img.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.company_status_img)

        self.company_name_text = QLabel(self.wrap_top)
        self.company_name_text.setObjectName(u"company_name_text")
        sizePolicy1.setHeightForWidth(self.company_name_text.sizePolicy().hasHeightForWidth())
        self.company_name_text.setSizePolicy(sizePolicy1)
        self.company_name_text.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.company_name_text.setFont(font)
        self.company_name_text.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.company_name_text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.company_status_text = QLabel(self.wrap_top)
        self.company_status_text.setObjectName(u"company_status_text")
        sizePolicy1.setHeightForWidth(self.company_status_text.sizePolicy().hasHeightForWidth())
        self.company_status_text.setSizePolicy(sizePolicy1)
        self.company_status_text.setMinimumSize(QSize(0, 0))
        self.company_status_text.setFont(font)
        self.company_status_text.setStyleSheet(u"color:grey")

        self.horizontalLayout_6.addWidget(self.company_status_text)

        self.company_status_b = QPushButton(self.wrap_top)
        self.company_status_b.setObjectName(u"company_status_b")
        self.company_status_b.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.company_status_b.setFont(font1)
        self.company_status_b.setStyleSheet(u"padding: 5px 10px")
        self.company_status_b.setFlat(False)

        self.horizontalLayout_6.addWidget(self.company_status_b, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.wrap_top, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.wrap_company = QGroupBox(self.wrapper)
        self.wrap_company.setObjectName(u"wrap_company")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.wrap_company.sizePolicy().hasHeightForWidth())
        self.wrap_company.setSizePolicy(sizePolicy3)
        self.wrap_company.setMinimumSize(QSize(0, 0))
        self.wrap_company.setSizeIncrement(QSize(0, 0))
        self.wrap_company.setFont(font)
        self.wrap_company.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.wrap_company.setFlat(False)
        self.wrap_company.setCheckable(False)
        self.wrap_company.setChecked(False)
        self.verticalLayout_4 = QVBoxLayout(self.wrap_company)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.widget = QWidget(self.wrap_company)
        self.widget.setObjectName(u"widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridWidget_3 = QWidget(self.widget)
        self.gridWidget_3.setObjectName(u"gridWidget_3")
        sizePolicy1.setHeightForWidth(self.gridWidget_3.sizePolicy().hasHeightForWidth())
        self.gridWidget_3.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.gridWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sync_main_next_text = QLabel(self.gridWidget_3)
        self.sync_main_next_text.setObjectName(u"sync_main_next_text")
        sizePolicy1.setHeightForWidth(self.sync_main_next_text.sizePolicy().hasHeightForWidth())
        self.sync_main_next_text.setSizePolicy(sizePolicy1)
        self.sync_main_next_text.setMinimumSize(QSize(0, 0))
        self.sync_main_next_text.setFont(font)
        self.sync_main_next_text.setStyleSheet(u"color:grey")

        self.gridLayout_4.addWidget(self.sync_main_next_text, 2, 1, 1, 1)

        self.sync_main_last_text = QLabel(self.gridWidget_3)
        self.sync_main_last_text.setObjectName(u"sync_main_last_text")
        sizePolicy1.setHeightForWidth(self.sync_main_last_text.sizePolicy().hasHeightForWidth())
        self.sync_main_last_text.setSizePolicy(sizePolicy1)
        self.sync_main_last_text.setMinimumSize(QSize(0, 0))
        self.sync_main_last_text.setFont(font)
        self.sync_main_last_text.setStyleSheet(u"color:grey")

        self.gridLayout_4.addWidget(self.sync_main_last_text, 1, 1, 1, 1)

        self.sync_main_text = QLabel(self.gridWidget_3)
        self.sync_main_text.setObjectName(u"sync_main_text")
        sizePolicy1.setHeightForWidth(self.sync_main_text.sizePolicy().hasHeightForWidth())
        self.sync_main_text.setSizePolicy(sizePolicy1)
        self.sync_main_text.setMinimumSize(QSize(0, 0))
        self.sync_main_text.setFont(font)

        self.gridLayout_4.addWidget(self.sync_main_text, 0, 1, 1, 1)

        self.sync_main_next_date = QLabel(self.gridWidget_3)
        self.sync_main_next_date.setObjectName(u"sync_main_next_date")
        sizePolicy1.setHeightForWidth(self.sync_main_next_date.sizePolicy().hasHeightForWidth())
        self.sync_main_next_date.setSizePolicy(sizePolicy1)
        self.sync_main_next_date.setFont(font)
        self.sync_main_next_date.setStyleSheet(u"color:grey")
        self.sync_main_next_date.setAlignment(Qt.AlignCenter)
        self.sync_main_next_date.setWordWrap(False)
        self.sync_main_next_date.setMargin(0)
        self.sync_main_next_date.setIndent(0)

        self.gridLayout_4.addWidget(self.sync_main_next_date, 2, 2, 1, 1)

        self.sync_main_date = QLabel(self.gridWidget_3)
        self.sync_main_date.setObjectName(u"sync_main_date")
        sizePolicy1.setHeightForWidth(self.sync_main_date.sizePolicy().hasHeightForWidth())
        self.sync_main_date.setSizePolicy(sizePolicy1)
        self.sync_main_date.setFont(font)
        self.sync_main_date.setAlignment(Qt.AlignCenter)
        self.sync_main_date.setWordWrap(False)
        self.sync_main_date.setMargin(0)
        self.sync_main_date.setIndent(0)

        self.gridLayout_4.addWidget(self.sync_main_date, 0, 2, 1, 1)

        self.sync_main_img = QLabel(self.gridWidget_3)
        self.sync_main_img.setObjectName(u"sync_main_img")
        self.sync_main_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_main_img.sizePolicy().hasHeightForWidth())
        self.sync_main_img.setSizePolicy(sizePolicy1)
        self.sync_main_img.setMaximumSize(QSize(20, 20))
        self.sync_main_img.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.sync_main_img.setFont(font2)
        self.sync_main_img.setPixmap(QPixmap(u":/assets/check_green.png"))
        self.sync_main_img.setScaledContents(True)

        self.gridLayout_4.addWidget(self.sync_main_img, 0, 0, 1, 1)

        self.sync_main_last_date = QLabel(self.gridWidget_3)
        self.sync_main_last_date.setObjectName(u"sync_main_last_date")
        sizePolicy1.setHeightForWidth(self.sync_main_last_date.sizePolicy().hasHeightForWidth())
        self.sync_main_last_date.setSizePolicy(sizePolicy1)
        self.sync_main_last_date.setFont(font)
        self.sync_main_last_date.setStyleSheet(u"color:grey")
        self.sync_main_last_date.setAlignment(Qt.AlignCenter)
        self.sync_main_last_date.setWordWrap(False)
        self.sync_main_last_date.setMargin(0)
        self.sync_main_last_date.setIndent(0)

        self.gridLayout_4.addWidget(self.sync_main_last_date, 1, 2, 1, 1)

        self.horizontalWidget = QWidget(self.gridWidget_3)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sync_main_run_b = QPushButton(self.horizontalWidget)
        self.sync_main_run_b.setObjectName(u"sync_main_run_b")
        sizePolicy1.setHeightForWidth(self.sync_main_run_b.sizePolicy().hasHeightForWidth())
        self.sync_main_run_b.setSizePolicy(sizePolicy1)
        self.sync_main_run_b.setFont(font1)
        self.sync_main_run_b.setStyleSheet(u"padding: 5px 10px")

        self.horizontalLayout_5.addWidget(self.sync_main_run_b, 0, Qt.AlignRight)


        self.gridLayout_4.addWidget(self.horizontalWidget, 3, 0, 1, 3)


        self.horizontalLayout_4.addWidget(self.gridWidget_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.gridWidget_4 = QWidget(self.widget)
        self.gridWidget_4.setObjectName(u"gridWidget_4")
        sizePolicy1.setHeightForWidth(self.gridWidget_4.sizePolicy().hasHeightForWidth())
        self.gridWidget_4.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.gridWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setContentsMargins(16, 0, 0, 0)
        self.sync_server_items_img = QLabel(self.gridWidget_4)
        self.sync_server_items_img.setObjectName(u"sync_server_items_img")
        self.sync_server_items_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_server_items_img.sizePolicy().hasHeightForWidth())
        self.sync_server_items_img.setSizePolicy(sizePolicy1)
        self.sync_server_items_img.setMinimumSize(QSize(20, 20))
        self.sync_server_items_img.setMaximumSize(QSize(20, 20))
        self.sync_server_items_img.setSizeIncrement(QSize(0, 0))
        self.sync_server_items_img.setFont(font2)
        self.sync_server_items_img.setPixmap(QPixmap(u":/assets/check_green.png"))
        self.sync_server_items_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_server_items_img, 0, 0, 1, 1)

        self.sync_server_items_text = QLabel(self.gridWidget_4)
        self.sync_server_items_text.setObjectName(u"sync_server_items_text")
        sizePolicy1.setHeightForWidth(self.sync_server_items_text.sizePolicy().hasHeightForWidth())
        self.sync_server_items_text.setSizePolicy(sizePolicy1)
        self.sync_server_items_text.setMinimumSize(QSize(0, 0))
        self.sync_server_items_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_server_items_text, 0, 1, 1, 1)

        self.sync_server_items_date = QLabel(self.gridWidget_4)
        self.sync_server_items_date.setObjectName(u"sync_server_items_date")
        sizePolicy1.setHeightForWidth(self.sync_server_items_date.sizePolicy().hasHeightForWidth())
        self.sync_server_items_date.setSizePolicy(sizePolicy1)
        self.sync_server_items_date.setFont(font)
        self.sync_server_items_date.setAlignment(Qt.AlignCenter)
        self.sync_server_items_date.setWordWrap(False)
        self.sync_server_items_date.setMargin(0)
        self.sync_server_items_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_server_items_date, 0, 2, 1, 1)

        self.sync_source_items_img = QLabel(self.gridWidget_4)
        self.sync_source_items_img.setObjectName(u"sync_source_items_img")
        self.sync_source_items_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_source_items_img.sizePolicy().hasHeightForWidth())
        self.sync_source_items_img.setSizePolicy(sizePolicy1)
        self.sync_source_items_img.setMaximumSize(QSize(20, 20))
        self.sync_source_items_img.setSizeIncrement(QSize(0, 0))
        self.sync_source_items_img.setFont(font2)
        self.sync_source_items_img.setPixmap(QPixmap(u":/assets/refresh.png"))
        self.sync_source_items_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_source_items_img, 1, 0, 1, 1)

        self.sync_source_items_text = QLabel(self.gridWidget_4)
        self.sync_source_items_text.setObjectName(u"sync_source_items_text")
        sizePolicy1.setHeightForWidth(self.sync_source_items_text.sizePolicy().hasHeightForWidth())
        self.sync_source_items_text.setSizePolicy(sizePolicy1)
        self.sync_source_items_text.setMinimumSize(QSize(0, 0))
        self.sync_source_items_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_source_items_text, 1, 1, 1, 1)

        self.sync_source_items_date = QLabel(self.gridWidget_4)
        self.sync_source_items_date.setObjectName(u"sync_source_items_date")
        sizePolicy1.setHeightForWidth(self.sync_source_items_date.sizePolicy().hasHeightForWidth())
        self.sync_source_items_date.setSizePolicy(sizePolicy1)
        self.sync_source_items_date.setFont(font)
        self.sync_source_items_date.setAlignment(Qt.AlignCenter)
        self.sync_source_items_date.setWordWrap(False)
        self.sync_source_items_date.setMargin(0)
        self.sync_source_items_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_source_items_date, 1, 2, 1, 1)

        self.sync_server_points_img = QLabel(self.gridWidget_4)
        self.sync_server_points_img.setObjectName(u"sync_server_points_img")
        self.sync_server_points_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_server_points_img.sizePolicy().hasHeightForWidth())
        self.sync_server_points_img.setSizePolicy(sizePolicy1)
        self.sync_server_points_img.setMaximumSize(QSize(20, 20))
        self.sync_server_points_img.setSizeIncrement(QSize(0, 0))
        self.sync_server_points_img.setFont(font2)
        self.sync_server_points_img.setPixmap(QPixmap(u":/assets/check_black.png"))
        self.sync_server_points_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_server_points_img, 2, 0, 1, 1)

        self.sync_server_points_text = QLabel(self.gridWidget_4)
        self.sync_server_points_text.setObjectName(u"sync_server_points_text")
        sizePolicy1.setHeightForWidth(self.sync_server_points_text.sizePolicy().hasHeightForWidth())
        self.sync_server_points_text.setSizePolicy(sizePolicy1)
        self.sync_server_points_text.setMinimumSize(QSize(0, 0))
        self.sync_server_points_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_server_points_text, 2, 1, 1, 1)

        self.sync_server_points_date = QLabel(self.gridWidget_4)
        self.sync_server_points_date.setObjectName(u"sync_server_points_date")
        sizePolicy1.setHeightForWidth(self.sync_server_points_date.sizePolicy().hasHeightForWidth())
        self.sync_server_points_date.setSizePolicy(sizePolicy1)
        self.sync_server_points_date.setFont(font)
        self.sync_server_points_date.setAlignment(Qt.AlignCenter)
        self.sync_server_points_date.setWordWrap(False)
        self.sync_server_points_date.setMargin(0)
        self.sync_server_points_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_server_points_date, 2, 2, 1, 1)

        self.sync_source_points_img = QLabel(self.gridWidget_4)
        self.sync_source_points_img.setObjectName(u"sync_source_points_img")
        self.sync_source_points_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_source_points_img.sizePolicy().hasHeightForWidth())
        self.sync_source_points_img.setSizePolicy(sizePolicy1)
        self.sync_source_points_img.setMaximumSize(QSize(20, 20))
        self.sync_source_points_img.setSizeIncrement(QSize(0, 0))
        self.sync_source_points_img.setFont(font2)
        self.sync_source_points_img.setPixmap(QPixmap(u":/assets/check_black.png"))
        self.sync_source_points_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_source_points_img, 3, 0, 1, 1)

        self.sync_source_points_text = QLabel(self.gridWidget_4)
        self.sync_source_points_text.setObjectName(u"sync_source_points_text")
        sizePolicy1.setHeightForWidth(self.sync_source_points_text.sizePolicy().hasHeightForWidth())
        self.sync_source_points_text.setSizePolicy(sizePolicy1)
        self.sync_source_points_text.setMinimumSize(QSize(0, 0))
        self.sync_source_points_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_source_points_text, 3, 1, 1, 1)

        self.sync_source_points_date = QLabel(self.gridWidget_4)
        self.sync_source_points_date.setObjectName(u"sync_source_points_date")
        sizePolicy1.setHeightForWidth(self.sync_source_points_date.sizePolicy().hasHeightForWidth())
        self.sync_source_points_date.setSizePolicy(sizePolicy1)
        self.sync_source_points_date.setFont(font)
        self.sync_source_points_date.setAlignment(Qt.AlignCenter)
        self.sync_source_points_date.setWordWrap(False)
        self.sync_source_points_date.setMargin(0)
        self.sync_source_points_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_source_points_date, 3, 2, 1, 1)

        self.sync_source_iip_img = QLabel(self.gridWidget_4)
        self.sync_source_iip_img.setObjectName(u"sync_source_iip_img")
        self.sync_source_iip_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_source_iip_img.sizePolicy().hasHeightForWidth())
        self.sync_source_iip_img.setSizePolicy(sizePolicy1)
        self.sync_source_iip_img.setMaximumSize(QSize(20, 20))
        self.sync_source_iip_img.setSizeIncrement(QSize(0, 0))
        self.sync_source_iip_img.setFont(font2)
        self.sync_source_iip_img.setPixmap(QPixmap(u":/assets/check_black.png"))
        self.sync_source_iip_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_source_iip_img, 4, 0, 1, 1)

        self.sync_source_iip_text = QLabel(self.gridWidget_4)
        self.sync_source_iip_text.setObjectName(u"sync_source_iip_text")
        sizePolicy1.setHeightForWidth(self.sync_source_iip_text.sizePolicy().hasHeightForWidth())
        self.sync_source_iip_text.setSizePolicy(sizePolicy1)
        self.sync_source_iip_text.setMinimumSize(QSize(0, 0))
        self.sync_source_iip_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_source_iip_text, 4, 1, 1, 1)

        self.sync_source_iip_date = QLabel(self.gridWidget_4)
        self.sync_source_iip_date.setObjectName(u"sync_source_iip_date")
        sizePolicy1.setHeightForWidth(self.sync_source_iip_date.sizePolicy().hasHeightForWidth())
        self.sync_source_iip_date.setSizePolicy(sizePolicy1)
        self.sync_source_iip_date.setFont(font)
        self.sync_source_iip_date.setAlignment(Qt.AlignCenter)
        self.sync_source_iip_date.setWordWrap(False)
        self.sync_source_iip_date.setMargin(0)
        self.sync_source_iip_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_source_iip_date, 4, 2, 1, 1)

        self.sync_server_iip_img = QLabel(self.gridWidget_4)
        self.sync_server_iip_img.setObjectName(u"sync_server_iip_img")
        self.sync_server_iip_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sync_server_iip_img.sizePolicy().hasHeightForWidth())
        self.sync_server_iip_img.setSizePolicy(sizePolicy1)
        self.sync_server_iip_img.setMaximumSize(QSize(20, 20))
        self.sync_server_iip_img.setSizeIncrement(QSize(0, 0))
        self.sync_server_iip_img.setFont(font2)
        self.sync_server_iip_img.setPixmap(QPixmap(u":/assets/check_black.png"))
        self.sync_server_iip_img.setScaledContents(True)

        self.gridLayout_5.addWidget(self.sync_server_iip_img, 5, 0, 1, 1)

        self.sync_server_iip_text = QLabel(self.gridWidget_4)
        self.sync_server_iip_text.setObjectName(u"sync_server_iip_text")
        sizePolicy1.setHeightForWidth(self.sync_server_iip_text.sizePolicy().hasHeightForWidth())
        self.sync_server_iip_text.setSizePolicy(sizePolicy1)
        self.sync_server_iip_text.setMinimumSize(QSize(0, 0))
        self.sync_server_iip_text.setFont(font)

        self.gridLayout_5.addWidget(self.sync_server_iip_text, 5, 1, 1, 1)

        self.sync_server_iip_date = QLabel(self.gridWidget_4)
        self.sync_server_iip_date.setObjectName(u"sync_server_iip_date")
        sizePolicy1.setHeightForWidth(self.sync_server_iip_date.sizePolicy().hasHeightForWidth())
        self.sync_server_iip_date.setSizePolicy(sizePolicy1)
        self.sync_server_iip_date.setFont(font)
        self.sync_server_iip_date.setAlignment(Qt.AlignCenter)
        self.sync_server_iip_date.setWordWrap(False)
        self.sync_server_iip_date.setMargin(0)
        self.sync_server_iip_date.setIndent(0)

        self.gridLayout_5.addWidget(self.sync_server_iip_date, 5, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.gridWidget_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_19 = QWidget(self.widget)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.widget_19)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setContentsMargins(16, 0, 0, 0)
        self.found_items_img = QLabel(self.widget_19)
        self.found_items_img.setObjectName(u"found_items_img")
        self.found_items_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.found_items_img.sizePolicy().hasHeightForWidth())
        self.found_items_img.setSizePolicy(sizePolicy1)
        self.found_items_img.setMaximumSize(QSize(20, 20))
        self.found_items_img.setSizeIncrement(QSize(0, 0))
        self.found_items_img.setFont(font)
        self.found_items_img.setPixmap(QPixmap(u":/assets/warning.png"))
        self.found_items_img.setScaledContents(True)

        self.gridLayout_6.addWidget(self.found_items_img, 0, 0, 1, 1)

        self.found_items_value = QLabel(self.widget_19)
        self.found_items_value.setObjectName(u"found_items_value")
        sizePolicy1.setHeightForWidth(self.found_items_value.sizePolicy().hasHeightForWidth())
        self.found_items_value.setSizePolicy(sizePolicy1)
        self.found_items_value.setFont(font)

        self.gridLayout_6.addWidget(self.found_items_value, 0, 4, 1, 1)

        self.found_points_img = QLabel(self.widget_19)
        self.found_points_img.setObjectName(u"found_points_img")
        self.found_points_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.found_points_img.sizePolicy().hasHeightForWidth())
        self.found_points_img.setSizePolicy(sizePolicy1)
        self.found_points_img.setMaximumSize(QSize(20, 20))
        self.found_points_img.setSizeIncrement(QSize(0, 0))
        self.found_points_img.setFont(font)
        self.found_points_img.setPixmap(QPixmap(u":/assets/warning.png"))
        self.found_points_img.setScaledContents(True)

        self.gridLayout_6.addWidget(self.found_points_img, 1, 0, 1, 1)

        self.found_price_img = QLabel(self.widget_19)
        self.found_price_img.setObjectName(u"found_price_img")
        self.found_price_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.found_price_img.sizePolicy().hasHeightForWidth())
        self.found_price_img.setSizePolicy(sizePolicy1)
        self.found_price_img.setMaximumSize(QSize(20, 20))
        self.found_price_img.setSizeIncrement(QSize(0, 0))
        self.found_price_img.setFont(font)
        self.found_price_img.setPixmap(QPixmap(u":/assets/check_black.png"))
        self.found_price_img.setScaledContents(True)

        self.gridLayout_6.addWidget(self.found_price_img, 2, 0, 1, 1)

        self.found_items_text = QLabel(self.widget_19)
        self.found_items_text.setObjectName(u"found_items_text")
        sizePolicy1.setHeightForWidth(self.found_items_text.sizePolicy().hasHeightForWidth())
        self.found_items_text.setSizePolicy(sizePolicy1)
        self.found_items_text.setMinimumSize(QSize(0, 0))
        self.found_items_text.setFont(font)

        self.gridLayout_6.addWidget(self.found_items_text, 0, 1, 1, 3)

        self.found_points_text = QLabel(self.widget_19)
        self.found_points_text.setObjectName(u"found_points_text")
        sizePolicy1.setHeightForWidth(self.found_points_text.sizePolicy().hasHeightForWidth())
        self.found_points_text.setSizePolicy(sizePolicy1)
        self.found_points_text.setMinimumSize(QSize(0, 0))
        self.found_points_text.setFont(font)

        self.gridLayout_6.addWidget(self.found_points_text, 1, 1, 1, 3)

        self.found_price_text = QLabel(self.widget_19)
        self.found_price_text.setObjectName(u"found_price_text")
        sizePolicy1.setHeightForWidth(self.found_price_text.sizePolicy().hasHeightForWidth())
        self.found_price_text.setSizePolicy(sizePolicy1)
        self.found_price_text.setMinimumSize(QSize(0, 0))
        self.found_price_text.setFont(font)

        self.gridLayout_6.addWidget(self.found_price_text, 2, 1, 1, 1)

        self.found_points_value = QLabel(self.widget_19)
        self.found_points_value.setObjectName(u"found_points_value")
        sizePolicy1.setHeightForWidth(self.found_points_value.sizePolicy().hasHeightForWidth())
        self.found_points_value.setSizePolicy(sizePolicy1)
        self.found_points_value.setFont(font)

        self.gridLayout_6.addWidget(self.found_points_value, 1, 4, 1, 1)

        self.found_price_value = QLabel(self.widget_19)
        self.found_price_value.setObjectName(u"found_price_value")
        sizePolicy1.setHeightForWidth(self.found_price_value.sizePolicy().hasHeightForWidth())
        self.found_price_value.setSizePolicy(sizePolicy1)
        self.found_price_value.setFont(font)

        self.gridLayout_6.addWidget(self.found_price_value, 2, 4, 1, 1)

        self.found_count_value = QLabel(self.widget_19)
        self.found_count_value.setObjectName(u"found_count_value")
        sizePolicy1.setHeightForWidth(self.found_count_value.sizePolicy().hasHeightForWidth())
        self.found_count_value.setSizePolicy(sizePolicy1)
        self.found_count_value.setFont(font)

        self.gridLayout_6.addWidget(self.found_count_value, 3, 4, 1, 1)

        self.found_count_text = QLabel(self.widget_19)
        self.found_count_text.setObjectName(u"found_count_text")
        sizePolicy1.setHeightForWidth(self.found_count_text.sizePolicy().hasHeightForWidth())
        self.found_count_text.setSizePolicy(sizePolicy1)
        self.found_count_text.setMinimumSize(QSize(0, 0))
        self.found_count_text.setFont(font)

        self.gridLayout_6.addWidget(self.found_count_text, 3, 1, 1, 1)

        self.found_count_img = QLabel(self.widget_19)
        self.found_count_img.setObjectName(u"found_count_img")
        self.found_count_img.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.found_count_img.sizePolicy().hasHeightForWidth())
        self.found_count_img.setSizePolicy(sizePolicy1)
        self.found_count_img.setMaximumSize(QSize(20, 20))
        self.found_count_img.setSizeIncrement(QSize(0, 0))
        self.found_count_img.setFont(font)
        self.found_count_img.setPixmap(QPixmap(u":/assets/warning.png"))
        self.found_count_img.setScaledContents(True)

        self.gridLayout_6.addWidget(self.found_count_img, 3, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_19, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.wrap_company)


        self.verticalLayout_3.addWidget(self.wrapper, 0, Qt.AlignTop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.company_name_text.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.company_status_text.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u043e\u0431\u043c\u0435\u043d \u0430\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.company_status_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.wrap_company.setTitle("")
        self.sync_main_next_text.setText(QCoreApplication.translate("Form", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0437\u0430\u043f\u0443\u0441\u043a", None))
        self.sync_main_last_text.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u043f\u043e\u043f\u044b\u0442\u043a\u0430", None))
        self.sync_main_text.setText(QCoreApplication.translate("Form", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.sync_main_next_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_main_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_main_img.setText("")
        self.sync_main_last_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_main_run_b.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.sync_server_items_img.setText("")
        self.sync_server_items_text.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.sync_server_items_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_source_items_img.setText("")
        self.sync_source_items_text.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0438\u0437 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None))
        self.sync_source_items_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_server_points_img.setText("")
        self.sync_server_points_text.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u043e\u0447\u0435\u043a \u043f\u0440\u043e\u0434\u0430\u0436 \u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.sync_server_points_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_source_points_img.setText("")
        self.sync_source_points_text.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u043b\u0430\u0434\u043e\u0432 \u0438\u0437 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None))
        self.sync_source_points_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_source_iip_img.setText("")
        self.sync_source_iip_text.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432 \u0438 \u0446\u0435\u043d \u0438\u0437 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430", None))
        self.sync_source_iip_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.sync_server_iip_img.setText("")
        self.sync_server_iip_text.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432 \u0438 \u0446\u0435\u043d \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.sync_server_iip_date.setText(QCoreApplication.translate("Form", u"12.05.2020 12:56", None))
        self.found_items_img.setText("")
        self.found_items_value.setText(QCoreApplication.translate("Form", u"12 \u0438\u0437 100", None))
        self.found_points_img.setText("")
        self.found_price_img.setText("")
        self.found_items_text.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.found_points_text.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043e \u0441\u043a\u043b\u0430\u0434\u043e\u0432", None))
        self.found_price_text.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0446\u0435\u043d \u0432 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0435", None))
        self.found_points_value.setText(QCoreApplication.translate("Form", u"12 \u0438\u0437 100", None))
        self.found_price_value.setText(QCoreApplication.translate("Form", u"100 \u0438\u0437 100", None))
        self.found_count_value.setText(QCoreApplication.translate("Form", u"12 \u0438\u0437 100", None))
        self.found_count_text.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432 \u0432 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0435", None))
        self.found_count_img.setText("")
    # retranslateUi

