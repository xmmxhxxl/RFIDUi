# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 11:33
# @Author : liman
# @File : main.py
# @Software : PyCharm
import time

from PyQt5.QtGui import *
from PyQt5.uic.properties import QtWidgets
from src.testserial import serialclass
from ui.uiProject import Ui_Form
from PyQt5.Qt import *
from PyQt5 import QtWidgets


class MyMainWindow(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.form3 = QtWidgets.QWidget()
        self.setupUi(self.form3)
        # self.name = username
        self.priceButton_2.clicked.connect(self.seekID)
        self.priceButton_3.clicked.connect(self.identifyID)

    def seekID(self):
        self.line = 0
        print("识别卡号")
        self.ID = self.priceArea_2.toPlainText()
        print("卡号是：", self.ID)
        self.tableWidget.insertRow(self.line)
        self.tableWidget.setItem(self.line, 0, QTableWidgetItem(self.ID))
        self.tableWidget.setItem(self.line, 1, QTableWidgetItem(self.usename))
        self.tableWidget.setItem(self.line, 2, QTableWidgetItem(time.asctime()))
        QApplication.processEvents()
        print("刷新界面")

    def identifyID(self):
        print("查找卡号")
        self.ID = self.priceArea_2.toPlainText()
        print("卡号是：", self.ID)

    def delID(self):
        print("删除卡号")
        self.delids = self.priceArea_3.toPlainText()
        print("要删除的卡号是:", self.delids)

    def showform(self, usename):
        print("show")
        self.usename = usename
        self.form3.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.showform()
    # window.show()
    sys.exit(app.exec_())
