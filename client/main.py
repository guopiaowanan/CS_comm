# ！/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from module import clientLogin

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    clientLogin.Ui_MainWindow_login().setupUi(w)

    w.show()

    sys.exit(app.exec_())
    pass

