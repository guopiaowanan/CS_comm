# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(90, 10, 181, 21))
        self.time.setStyleSheet("background-color: rgb(199, 255, 243);")
        self.time.setObjectName("time")
        self.phoneLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLogin.setGeometry(QtCore.QRect(100, 80, 171, 20))
        self.phoneLogin.setObjectName("phoneLogin")
        self.pswLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.pswLogin.setGeometry(QtCore.QRect(100, 140, 171, 20))
        self.pswLogin.setObjectName("pswLogin")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.phoneLogin, self.pswLogin)
        MainWindow.setTabOrder(self.pswLogin, self.loginBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time.setText(_translate("MainWindow", "当前时间"))
        self.loginBtn.setText(_translate("MainWindow", "登录"))
