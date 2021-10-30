# -*- codeing = utf-8 -*-
# @Time : 2021/10/28 21:04
# @Author : liman
# @File : bindDataUi.py
# @Software : PyCharm
import sys
import time

import cv2 as cv
import serial
from PyQt5.QtGui import *
from time import sleep
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

        #   实例化读取卡号线程
        self.readid = ReadID()
        self.readid._sinid.connect(self.showId)
        self.readid.start()

        # 按键槽函数
        self.priceButton_2.clicked.connect(self.Screenshot)

        self.count = 0

        # 链接数据库
        self.msq = MysqlHelper(host='120.24.222.48', user='root', password='root', database='informatioBase')

        # 多线程打开文件,防止卡顿
        self.openface = ReadFace()
        self.openface.readSin.connect(self.insertInformation)
        # self.openface.start()

    # 返回查找结果
    def finResult(self):
        self.idlist = []
        self.select_all = self.msq.select_all('select stu_num from informaTable')
        for item in self.select_all:
            self.idlist.append(item[0])
            # print(item[0])
        return self.idlist

    def showimage(self):
        QApplication.processEvents()

    # 截图函数
    def Screenshot(self):
        try:
            self.count += 1
            self.thread.playFlag = 0
            # self.openface.runRead = 0
            cv.imwrite('../faceID/img/ScreeFace.png', self.thread.image)
            if self.count == 2:
                self.thread.playFlag = 1
                self.count = 0
                self.openface.runRead = 1  # 读取文件
                self.openface.start()
        except Exception as ex:
            print("截图异常！位置:UseBinData->Screenshot!", ex)

    # 显示卡号
    def showId(self):
        try:
            self.stu_id.setPlainText(str(self.readid.data.encode().hex()))
            QApplication.processEvents()
        except Exception as ex:
            print("显示异常！位置:UseBinData->showId!", ex)

    # 插入数据到数据库中
    def insertInformation(self, faceID):
        try:
            self.number = self.stu_num.toPlainText()  # 获取学号
            self.name = self.stu_name.toPlainText()  # 获取姓名
            self.stuclass = self.stu_class.toPlainText()  # 获取班级
            self.id = self.stu_id.toPlainText()  # 获取卡号
            if self.name == '' or self.number == '' or self.stuclass == '' or self.id == '':
                QMessageBox.critical(self, 'Wrong', '请输入正确的信息!')
            else:
                idresult = self.finResult()
                print("查询结果", idresult)
                if self.number in idresult:
                    QMessageBox.critical(self, 'Wrong', '该学号已绑定!')
                else:
                    self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化获取当前时间
                    self.user = "用户自助绑定"
                    self.stu_id.clear()
                    self.stu_num.clear()
                    self.stu_class.clear()
                    self.stu_name.clear()
                    print(self.number, self.name, self.stuclass, self.id)
                    QApplication.processEvents()
                    # print(faceID)
                    # 插入数据到数据库中
                    self.msq.insert('insert into informaTable(stu_num,stu_name,stu_class,stu_info,stu_id,add_time,'
                                    'administrator) values(%s,%s,%s,%s,%s,%s,%s)',
                                    [self.number, self.name, self.stuclass, faceID, self.id, self.time, self.user])
                    print("数据插入成功!")
                    QMessageBox.information(self, 'Right', '绑定成功!')
                    self.openface.runRead = 0  # 停止读取
        except Exception as ex:
            print("插入数据库异常! 位置:UseBinData->insertInformation", ex)


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
        try:
            self.cap = cv.VideoCapture(0)  # 打开摄像头
            while True:
                if self.playFlag:
                    grabeed, self.image = self.cap.read()  # 获取视频流
                    self.showfarm = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_BGR888)
                    self.playLabel.setPixmap(QPixmap.fromImage(self.showfarm))
                    self._sinout.emit()
        except Exception as ex:
            print("获取视频流异常!位置:MyThread->run", ex)


# 多线程读取卡号
class ReadID(QThread):
    _sinid = pyqtSignal()

    def __init__(self, parent=None):
        super(QThread, self).__init__(parent)
        try:
            self.ser = self.ser = serial.Serial("com13", 115200, timeout=0.5)
        except Exception as ex:
            print("获取视频流异常!位置:ReadID->__init__", ex)

    def rec(self, ser):
        try:
            while True:
                dataid = ser.read_all().decode()
                if dataid == '':
                    continue
                else:
                    break
                    sleep(0.02)
            return dataid
        except Exception as ex:
            print("读取卡号异常! 位置:ReadID->rec", ex)

    def run(self):
        try:
            if self.ser.isOpen():
                print("open")
            else:
                print("not")
            while True:
                self.data = self.rec(self.ser)
                if self.data != b'':
                    print("data:", self.data)
                    print("解码", self.data.encode().hex())
                    if self.data == b'x':
                        print("exit")
                        break
                self._sinid.emit()
        except Exception as ex:
            print("解码异常! 位置:ReadID->run")


# 多线程读取文件
class ReadFace(QThread):
    readSin = pyqtSignal(object)

    def __init__(self):
        super(ReadFace, self).__init__()
        self.runRead = 0  # 控制线程

    def run(self):
        try:
            print("读取文件!")
            fb = open('../faceID/img/ScreeFace.png', 'rb')
            self.face = fb.read()
            fb.close()
            self.readSin.emit(self.face)
        except Exception as ex:
            print("读取文件异常! 位置:ReadFace->run", ex)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = UseBinData()
    window.show()
    sys.exit(app.exec_())
