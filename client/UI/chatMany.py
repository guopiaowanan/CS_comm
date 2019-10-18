# ！/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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

        self.single = QtWidgets.QPushButton(self.centralwidget)
        self.single.setGeometry(QtCore.QRect(440, 435, 61, 31))
        self.single.setObjectName("single")

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chats.setHtml(_translate("MainWindow", "聊天内容"))
        self.label.setText(_translate("MainWindow", "正在群聊："))
        self.sends.setText(_translate("MainWindow", "发送"))
        self.single.setText(_translate("MainWindow", "私聊"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(w)
    w.show()

    sys.exit(app.exec_())
    pass
