# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 11:33
# @Author : liman
# @File : mainWindos.py
# @Software : PyCharm
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.testserial import serialclass
from ui.uiProject import Ui_Form


class MyMainWindow(QWidget, Ui_Form):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    im = MyMainWindow()
    im.show()
    sys.exit(app.exec_())
