# -*- codeing = utf-8 -*-
# @Time : 2021/10/28 21:04
# @Author : liman
# @File : bindDataUi.py
# @Software : PyCharm
import sys
import cv2 as cv
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from ui.userui import Ui_Form
from src.MysqlHelper import MysqlHelper


class UseBinData(QWidget, Ui_Form):

    def __init__(self):
        super(UseBinData, self).__init__()
        self.setupUi(self)

        # 实例化视频流线程
        self.thread = MyThread()
        self.thread.playLabel = self.label
        self.thread._sinout.connect(self.showimage)
        self.thread.start()

        # 按键槽函数
        self.priceButton_2.clicked.connect(self.Screenshot)

        self.count = 0

    def showimage(self):
        QApplication.processEvents()

    def Screenshot(self):
        self.count += 1
        self.thread.playFlag = 0
        cv.imwrite('../faceID/img/ScreeFace.png', self.thread.image)
        if self.count == 2:
            self.thread.playFlag = 1
            self.count = 0


# 多线程显示视频流
class MyThread(QThread):
    _sinout = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        print("线程初始化")
        self.playLabel = QLabel()
        self.stuid = QTextEdit()
        self.stuname = QTextEdit()
        self.stuclass = QTextEdit()
        self.playFlag = 1  # 控制线程

    def run(self):
        self.cap = cv.VideoCapture(0)  # 打开摄像头
        while True:
            if self.playFlag:
                grabeed, self.image = self.cap.read()  # 获取视频流
                self.showfarm = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_BGR888)
                self.playLabel.setPixmap(QPixmap.fromImage(self.showfarm))
                self._sinout.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = UseBinData()
    window.show()
    sys.exit(app.exec_())
