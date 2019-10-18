# ！/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, re, socket, json
import function
import chatGroup, clientReg





class Ui_MainWindow_login(QtWidgets.QWidget):
    """
    登录界面
    """
    def __init__(self):
        self.addr = ("127.0.0.1",9999)
        self.sock = socket.socket()
        self.sock.connect(self.addr)        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(100, 10, 171, 21))
        self.time.setStyleSheet("background-color: rgb(199, 255, 243);")
        self.time.setObjectName("time")

        #定时器显示时间
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start(1000)

        # 登录输入框
        self.loginLabel = QtWidgets.QLabel(MainWindow)
        self.loginLabel.setGeometry(QtCore.QRect(60, 80, 80, 19))
        self.loginLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.loginLabel.setObjectName("loginLabel")
        self.loginLabel.setText(" 手机号/邮箱：")
        self.phoneLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLogin.setGeometry(QtCore.QRect(150, 80, 171, 20))
        self.phoneLogin.setObjectName("phoneLogin")

        # 登录密码输入框
        self.pswLabel = QtWidgets.QLabel(MainWindow)
        self.pswLabel.setGeometry(QtCore.QRect(60, 140, 80, 19))
        self.pswLabel.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.pswLabel.setText("  密  码  ：")
        self.pswLabel.setObjectName("pswLabel")
        self.pswLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.pswLogin.setGeometry(QtCore.QRect(150, 140, 171, 20))
        self.pswLogin.setObjectName("pswLogin")

        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(95, 210, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.released.connect(lambda : self.onLoginBtnClicked())

        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.regBtn.setObjectName("loginBtn")
        self.regBtn.released.connect(lambda : self.onRegBtnClicked())

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


    def loginRequest(self,phone):
        """
        发送登录验证消息
        """
        self.phone = phone

        self.req = json.dumps(self.req)
        self.reqLen = "{:<15}".format(len(self.req)).encode()
        self.sock.send(self.reqLen)
        self.sock.send(self.req.encode())
        print("验证消息已发送")
        self.rspLen = int(self.sock.recv(15).decode().strip())
        if self.rspLen :
            self.recvSize = 0
            self.jsonData = b""
        while self.recvSize < self.rspLen:     # 接收json请求           
            self.tmpData = self.sock.recv(self.rspLen-self.recvSize)
            if not self.tmpData:
                break
            else:
                self.recvSize += len(self.tmpData)
                self.jsonData += self.tmpData
        
        self.jsonData = json.loads(self.jsonData.decode())
        print(self.jsonData)
        
        # 打开群聊界面
        self.login_app = QtWidgets.QApplication(sys.argv)
        self.reg = QtWidgets.QMainWindow()
        chatGroup.Ui_MainWindow_chats(self.sock,self.phone).setupUi(self.reg)
        self.reg.show()

    def onLoginBtnClicked(self):
        """
        登录按钮事件
        """ 
        self.phoneOrEmail = self.phoneLogin.text()
        self.password = function.getMd5(self.pswLogin.text()).upper()
        self.req = {"op": 11, "args": {"uLogin": self.phoneOrEmail,"password":self.password}}

        if re.match(r'1\d{10}',self.phoneOrEmail):
            self.req["op"] = 12
            self.loginRequest(self.phoneOrEmail)
            
        
        elif re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z]+)+$',self.phoneOrEmail):
            self.req["op"] = 11
            self.loginRequest(self.phoneOrEmail)

        else:
            self.loginLabel.setText(" 账号格式有误")
        
        return 
        

    def onRegBtnClicked(self):
        """
        注册按钮事件
        """

        self.reg = QtWidgets.QMainWindow()
        clientReg.Ui_Form().setupUi(self.reg)
        self.reg.show()

    def onTimeout(self):
        """
        时间
        """
        self.time.setText("   当前时间：" + time.strftime("%H:%M:%S"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.loginBtn.setText(_translate("MainWindow", "登录"))
        self.regBtn.setText(_translate("MainWindow", "注册"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    Ui_MainWindow_login().setupUi(w)
    

    w.show()

    sys.exit(app.exec_())
    pass


