# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatSingle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.friends = QtWidgets.QLabel(self.centralwidget)
        self.friends.setEnabled(False)
        self.friends.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.friends.setStyleSheet("background-color: rgb(209, 255, 194);")
        self.friends.setObjectName("friends")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(410, 350, 61, 21))
        self.send.setObjectName("send")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 320, 341, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.chat = QtWidgets.QTextBrowser(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(30, 70, 461, 231))
        self.chat.setObjectName("chat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.friends.setText(_translate("MainWindow", "好友名字"))
        self.send.setText(_translate("MainWindow", "发送"))
