# ！/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    """
    注册界面
    """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 350)

        #注册按钮
        self.regBtn = QtWidgets.QPushButton(Form)
        self.regBtn.setGeometry(QtCore.QRect(280, 276, 75, 23))
        self.regBtn.setObjectName("regBtn")

        # 用户名
        self.unameLabel = QtWidgets.QLabel(Form)
        self.unameLabel.setGeometry(QtCore.QRect(30, 30, 80, 19))
        self.unameLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.unameLabel.setObjectName("unameLabel")
        self.uname = QtWidgets.QLineEdit(Form)
        self.uname.setGeometry(QtCore.QRect(120, 30, 131, 21))
        self.uname.setText("")
        self.uname.setObjectName("uname")

        # 手机号
        self.phoneLabel = QtWidgets.QLabel(Form)
        self.phoneLabel.setGeometry(QtCore.QRect(30, 80, 80, 19))
        self.phoneLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.phoneLabel.setObjectName("label")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(120, 80, 130, 21))
        self.phone.setText("")
        self.phone.setObjectName("phone")

        # 验证码
        self.checkCordLabel = QtWidgets.QLabel(Form)
        self.checkCordLabel.setGeometry(QtCore.QRect(30, 130, 80, 19))
        self.checkCordLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.checkCordLabel.setObjectName("checkCordLabel")
        self.checkCord = QtWidgets.QLineEdit(Form)
        self.checkCord.setGeometry(QtCore.QRect(120, 130, 130, 21))
        self.checkCord.setText("")
        self.checkCord.setObjectName("checkCord")

        # 邮箱
        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(30, 180, 80, 19))
        self.emailLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.emailLabel.setObjectName("emailLabel")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(120, 180, 130, 21))
        self.email.setText("")
        self.email.setObjectName("email")
        
        # 邮箱验证码
        self.checkEmailCordLabel = QtWidgets.QLabel(Form)
        self.checkEmailCordLabel.setGeometry(QtCore.QRect(30, 230, 80, 19))
        self.checkEmailCordLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.checkEmailCordLabel.setObjectName("checkCordLabel")
        self.checkEmailCord = QtWidgets.QLineEdit(Form)
        self.checkEmailCord.setGeometry(QtCore.QRect(120, 230, 130, 21))
        self.checkEmailCord.setText("")
        self.checkEmailCord.setObjectName("checkCord")

        # 密码
        self.pswLabel = QtWidgets.QLabel(Form)
        self.pswLabel.setGeometry(QtCore.QRect(30, 280, 80, 19))
        self.pswLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.pswLabel.setObjectName("pswLabel")
        self.psw = QtWidgets.QLineEdit(Form)
        self.psw.setGeometry(QtCore.QRect(120, 280, 130, 21))
        self.psw.setText("")
        self.psw.setObjectName("psw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.regBtn.setText(_translate("Form", "注册"))
        self.unameLabel.setText(_translate("MainWindow", " 用户名："))
        self.phoneLabel.setText(_translate("MainWindow", " 手机号："))
        self.checkCordLabel.setText(_translate("MainWindow", " 验证码："))
        self.emailLabel.setText(_translate("MainWindow", " 邮 箱："))
        self.checkEmailCordLabel.setText(_translate("MainWindow", " 邮箱验证码："))
        self.pswLabel.setText(_translate("MainWindow", " 密 码："))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    Ui_Form().setupUi(w)

    w.show()

    sys.exit(app.exec_())
    pass
