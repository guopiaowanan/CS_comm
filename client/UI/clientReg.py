# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientReg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.regBtn = QtWidgets.QPushButton(Form)
        self.regBtn.setGeometry(QtCore.QRect(260, 220, 75, 23))
        self.regBtn.setObjectName("regBtn")
        self.checkCord = QtWidgets.QLineEdit(Form)
        self.checkCord.setGeometry(QtCore.QRect(50, 130, 131, 21))
        self.checkCord.setText("")
        self.checkCord.setObjectName("checkCord")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(50, 180, 131, 21))
        self.email.setText("")
        self.email.setObjectName("email")
        self.uname = QtWidgets.QLineEdit(Form)
        self.uname.setGeometry(QtCore.QRect(50, 30, 131, 21))
        self.uname.setText("")
        self.uname.setObjectName("uname")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(50, 80, 131, 21))
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.email_2 = QtWidgets.QLineEdit(Form)
        self.email_2.setGeometry(QtCore.QRect(50, 220, 131, 21))
        self.email_2.setText("")
        self.email_2.setObjectName("email_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.regBtn.setText(_translate("Form", "注册"))
