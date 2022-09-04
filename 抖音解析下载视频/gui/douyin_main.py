# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'douyin_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 698)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setBaseSize(QSize(200, 400))
        font = QFont()
        font.setFamily(u"\u534e\u6587\u884c\u6977")
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setMidLineWidth(2)
        self.E_shuru = QLineEdit(self.frame)
        self.E_shuru.setObjectName(u"E_shuru")
        self.E_shuru.setGeometry(QRect(20, 40, 381, 31))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 451, 31))
        self.QB_APP = QRadioButton(self.frame)
        self.QB_APP.setObjectName(u"QB_APP")
        self.QB_APP.setGeometry(QRect(410, 40, 111, 31))
        self.QB_APP.setAutoExclusive(False)
        self.QB_logo = QRadioButton(self.frame)
        self.QB_logo.setObjectName(u"QB_logo")
        self.QB_logo.setGeometry(QRect(520, 40, 141, 31))
        self.QB_logo.setAutoExclusive(False)
        self.PB_kaishi = QPushButton(self.frame)
        self.PB_kaishi.setObjectName(u"PB_kaishi")
        self.PB_kaishi.setGeometry(QRect(670, 20, 101, 41))
        self.save_pb = QPushButton(self.frame)
        self.save_pb.setObjectName(u"save_pb")
        self.save_pb.setGeometry(QRect(780, 10, 141, 61))
        font1 = QFont()
        font1.setFamily(u"\u534e\u6587\u884c\u6977")
        font1.setPointSize(14)
        self.save_pb.setFont(font1)

        self.verticalLayout.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.PB_kaishi.clicked.connect(MainWindow.smain)
        # self.tableWidget.cellClicked.connect(MainWindow.smain)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6296\u97f3\u77ed\u89c6\u9891", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5206\u4eab\u7684\u4e3b\u9875\u6216\u8005\u89c6\u9891\u94fe\u63a5", None))
        self.QB_APP.setText(QCoreApplication.translate("MainWindow", u"APP", None))
        self.QB_logo.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u6c34\u5370", None))
        self.PB_kaishi.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.save_pb.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u4e0b\u8f7d\u8def\u5f84", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u4f5c\u8005", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5730\u5740", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u540d\u79f0", None));
    # retranslateUi

