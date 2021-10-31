# -*- codeing = utf-8 -*-
# @Time : 2021/10/29 22:36
# @Author : liman
# @File : useingUi.py
# @Software : PyCharm
import base64
import json
import time

import cv2 as cv
import requests
import serial
from PyQt5.QtGui import *
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from aip import AipFace

from src.faceComparison import Face
from ui.useInterface import Ui_Form
from src.MysqlHelper import MysqlHelper


class UseSingData(QWidget, Ui_Form):

    def __init__(self):
        super(UseSingData, self).__init__()
        self.setupUi(self)

        # 实例化视频流线程
        self.thread = MyThread()
        self.thread.playLabel = self.label
        self.thread._sinout.connect(self.showimage)
        self.thread.start()

        #   实例化读取卡号线程
        self.readid = ReadID()
        self.readid._sinid.connect(self.Result)
        self.readid.start()

        self.count = 0

        # 链接数据库
        self.msq = MysqlHelper(host='120.24.222.48', user='root', password='root', database='informatioBase')

        # 人脸数据比对线程
        self.result = ComparisonFace()
        self.result.comparisonSin.connect(self.faceResult)

    def showimage(self):
        QApplication.processEvents()

    # 多线程识别卡号信号槽
    def faceResult(self, comparisonScore, error_code):
        print("comparisonScore:", comparisonScore)
        print("error_code:", error_code)
        self.stu_id_3.clear()
        if error_code == 0:
            print("有人脸信息！")
            if comparisonScore >= 85:
                self.stu_id_3.setText("是")
            else:
                QMessageBox.critical(self, 'Wrong', '不是本人!')
                self.stu_id_3.setText("否")
        else:
            QMessageBox.critical(self, 'Wrong', '请将人脸对准摄像头!')
            print("没有人脸信息！")
        QApplication.processEvents()

    # 显示卡号
    def Result(self):
        try:
            self.stu_id.clear()
            self.stu_id_2.clear()
            self.stu_id_7.clear()
            self.findResult = self.readid.findResult
            self.ID = self.findResult[0]
            print(self.findResult[0])
            fout = open('../faceID/mysqlDownload/downloadFace.png', 'wb')
            fout.write(self.findResult[3])
            fout.close()
            self.stu_id.setText(self.findResult[0])  # 显示卡号关联的学号
            self.stu_id_2.setText(self.findResult[1])  # 显示卡号关联的姓名
            self.stu_id_7.setText(self.findResult[2])  # 显示卡号关联的班级
            cv.imwrite('../faceID/ScreeFace/ScreeFace.png', self.thread.image)
            self.result.start()
            QApplication.processEvents()
        except Exception as ex:
            print("显示异常!位置:UseBinData->Result!", ex)


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

            # 链接数据库
            self.msq = MysqlHelper(host='120.24.222.48', user='root', password='root', database='informatioBase')
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
                    stuID = self.data.encode().hex()
                    self.findResult = self.msq.select_one('select * from informaTable where stu_id=%s', [stuID])
                    if self.data == b'x':
                        print("exit")
                        break
                self._sinid.emit()
        except Exception as ex:
            print("解码异常! 位置:ReadID->run")


# 多线程比对人脸
class ComparisonFace(QThread):
    comparisonSin = pyqtSignal(object, object)

    def __init__(self):
        super(ComparisonFace, self).__init__()
        self.APP_ID = '25065352'
        self.APP_KEY = 'gDjVAHz8CkxIvvh4Dii1Nb7C'
        self.SK = 'dVdid50k3xNylRLDh5SsM7zsn0gNV2Pm'
        self.bas = 'BASE64'
        self.client = AipFace(self.APP_ID, self.APP_KEY, self.SK)

    def run(self):
        print("进入比对线程!")
        try:
            with open("../faceID/mysqlDownload/downloadFace.png", "rb") as f1:
                pic1 = f1.read()
                f1.close()
            with open("../faceID/ScreeFace/ScreeFace.png", "rb") as f2:
                pic2 = f2.read()
                f2.close()
            image_data = json.dumps([
                {"image": str(base64.b64encode(pic1), "utf-8"), "image_type": "BASE64"},
                {"image": str(base64.b64encode(pic2), "utf-8"), "image_type": "BASE64"}
            ])
            # print(image_data)
            # 2.拼接人脸识别API接口
            get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(
                self.APP_KEY, self.SK)

            API_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="

            text = requests.get(get_token).json()
            print(text['access_token'])

            url = API_url + text['access_token']
            print(url)
            # 3.请求API接口传入json数据，返回图片相似度
            self.response = requests.post(url, image_data).json()

            print(self.response)
            error_code = self.response['error_code']
            print("错误码为", error_code)
            score = self.response['result']['score']

            error_msg = self.response['error_msg']
            print("相似度为：{}%".format(score))

            print("error_msg:", error_msg)
            self.comparisonSin.emit(score, error_code)
        except Exception as ex:
            self.comparisonSin.emit(0, error_code)
            print("人脸比对异常! 位置:ComparisonFace->run 异常信息:{}".format(ex))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = UseSingData()
    window.show()
    sys.exit(app.exec_())
