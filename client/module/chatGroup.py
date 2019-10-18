# ！/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import chatSingle
import socket, json


class Ui_MainWindow_chats(QtWidgets.QWidget):
    """
    群聊ui
    """
    def __init__(self,sock,phone):
        self.sock = sock
        self.phone = phone
        print(self.sock,self.phone)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.msgs = QtWidgets.QTextEdit(self.centralwidget)
        self.msgs.setGeometry(QtCore.QRect(30, 400, 381, 71))
        self.msgs.setObjectName("msgs")
        self.chats = QtWidgets.QTextBrowser(self.centralwidget)
        self.chats.setGeometry(QtCore.QRect(30, 70, 501, 301))
        self.chats.setObjectName("chats")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 21))
        self.label.setStyleSheet("background-color: rgb(255, 250, 205);\n"
"border-color: rgb(44, 37, 255);")
        self.label.setObjectName("label")

        self.sends = QtWidgets.QPushButton(self.centralwidget)
        self.sends.setGeometry(QtCore.QRect(440, 405, 61, 31))
        self.sends.setObjectName("sends")
        self.sends.released.connect(lambda : self.onSendsClicked())

        self.single = QtWidgets.QPushButton(self.centralwidget)
        self.single.setGeometry(QtCore.QRect(440, 435, 61, 31))
        self.single.setObjectName("single")
        self.single.released.connect(lambda : self.on_single_clicked())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        MainWindow.show()

    def onSendsClicked(self):
        """
        功能：群聊消息发送
        """
        # 待发送消息
        self.message = self.msgs.toPlainText()
        self.msgs.clear()
        self.req = {"op": 31, "args": {"from": self.phone, "to": "group","content": self.message}}
        self.req = json.dumps(self.req)
        # 发送群聊消息
        self.reqLen = "{:<15}".format(len(self.req)).encode()
        self.sock.send(self.reqLen)
        self.sock.send(self.req.encode())
        print(self.req)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chats.setHtml(_translate("MainWindow", "聊天内容"))
        self.label.setText(_translate("MainWindow", "正在群聊："))
        self.sends.setText(_translate("MainWindow", "发送"))
        self.single.setText(_translate("MainWindow", "私聊"))
    
    def on_single_clicked(self):
        """
        私聊按钮事件
        """
        print("单人聊天")
        # self.single_app = QtWidgets.QApplication(sys.argv)
        self.single = QtWidgets.QMainWindow()
        chatSingle.Ui_MainWindow_chat().setupUi(self.single)

        self.single.show()

if __name__ == "__main__":
    import sys

    sock = None
    phone = None

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    Ui_MainWindow_chats(sock,phone).setupUi(w)
    w.show()

    sys.exit(app.exec_())
    pass
