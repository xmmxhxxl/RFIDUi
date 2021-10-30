# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 11:33
# @Author : liman
# @File : faceComparison.py
# @Software : PyCharm
import time

import serial
from PyQt5.QtGui import *
from PyQt5.uic.properties import QtWidgets
from ui.uiProject import Ui_Form
from PyQt5.Qt import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.MysqlHelper import MysqlHelper
from src.faceComparison import Face


class MyMainWindow(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.form3 = QtWidgets.QWidget()
        self.setupUi(self.form3)
        # self.name = username
        # self.thread = WorkTheard()
        self.confirm_but.clicked.connect(self.seekID)  # 添加卡信号槽
        self.del_but.clicked.connect(self.delID)  # 删除卡的信号槽
        self.renovate_but.clicked.connect(self.queryIfon)  # 刷新界面
        self.openface_but.clicked.connect(self.openFace)  # 打开人脸数据
        # self.priceButton_4.clicked.connect(self.findID)

        self.helper = MysqlHelper(host='120.24.222.48', database='informatioBase', user='root',
                                  password='root')  # 链接数据库
        # self.showtable()  # 显示数据库中的数据

        #   实例化读取卡号线程
        self.readid = ReadID()
        self.readid._sinid.connect(self.showId)
        self.readid.start()

        # 多线程打开文件，防止卡顿
        # self.openface = ReadFace()
        # self.openface.readSin.connect(self.seekID)
        # self.openface.start()
        # self.insertCount = 0

        # 多线程查询数据，防止界面卡死
        self.showMain = showMainWindos()
        self.showMain.showSin.connect(self.showtable)
        self.count = 0
        self.showMain.start()

    #   刷新表单数据
    def showtable(self, select_all):
        try:
            i = 0
            self.line = 0
            self.select_all = select_all
            for item in self.select_all:
                face_pic = QLabel()
                image = item[3]
                # print(self.image)
                fout = open('../faceID/img/mysqlface{}.png'.format(i), 'wb')
                fout.write(image)
                fout.close()
                face_pic.setPixmap(QPixmap('../faceID/img/mysqlface{}.png'.format(i)))  # 获取图片路径

                print(item[0], item[1], item[2], item[4], item[5], item[6])
                self.tableWidget.insertRow(self.line)
                self.tableWidget.setItem(self.line, 0, QTableWidgetItem(str(item[0])))
                self.tableWidget.setItem(self.line, 1, QTableWidgetItem(item[1]))
                self.tableWidget.setItem(self.line, 2, QTableWidgetItem(item[2]))
                self.tableWidget.setCellWidget(self.line, 3, face_pic)
                print(i)
                self.tableWidget.setItem(self.line, 4, QTableWidgetItem(item[4]))
                self.tableWidget.setItem(self.line, 5, QTableWidgetItem(item[6]))
                self.tableWidget.setItem(self.line, 6, QTableWidgetItem(item[5]))
                i += 1
            QApplication.processEvents()  # 刷新表单数据
            i = 0
        except Exception as ex:
            print("显示数据异常! 位置:MyMainWindow->showtable", ex)

    # 显示卡号
    def showId(self):
        try:
            self.sut_id.setPlainText(str(self.readid.data.encode().hex()))
            QApplication.processEvents()
        except Exception as ex:
            print("显示异常!位置:UseBinData->showId! 异常信息:{}".format(ex))

    def openFace(self):
        self.faceDir = QFileDialog.getOpenFileName(self, 'Open file', '.png')
        print(self.faceDir[0], '   ', type(self.faceDir))
        # dir = ''.join(self.faceDir)
        # print(dir, '   ', type(dir))
        if self.faceDir[0]:
            f = open(self.faceDir[0], 'rb')
            self.faceDirIfon = f.read()

    def queryIfon(self):
        try:
            self.count += 1
            if self.count == 1:
                self.showMain.runShow = 1
                self.count = 0
        except Exception as ex:
            print("查询数据库异常! 位置:MyMainWindow->queryIfon", ex)

    def insertInfo(self):
        try:
            self.insertCount += 1
            if self.insertCount == 1:
                self.openface.runRead = 1
                self.insertCount = 0
        except Exception as ex:
            print("文件读取异常! 位置:MyMainWindow->insertInfo", ex)

    # 获取数据并插入到数据库中
    def seekID(self):
        try:
            # self.openface.runRead = 0
            print("识别卡号")
            self.ID = self.sut_id.toPlainText()  # 获取卡号
            self.stunum = self.stu_num.toPlainText()  # 获取学号
            self.stuname = self.name.toPlainText()  # 获取姓名
            self.stuclass = self.classes.toPlainText()  # 获取班级信息
            # 获取信息之后清空label
            self.sut_id.clear()
            self.stu_num.clear()
            self.name.clear()
            self.classes.clear()

            self.stu_info = self.faceDirIfon
            self.face_pic = QLabel()
            self.face_pic.setPixmap(QPixmap(''.join(self.faceDir[0])))  # 获取图片路径

            self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化获取当前时间
            self.rowcount = self.tableWidget.rowCount()  # 获取当前表格的行数
            print(
                "姓名:{},学号:{},班级:{},卡号:{},管理员:{},时间:{}".format(self.stuname, self.stunum, self.stuclass,
                                                              self.ID,
                                                              self.usename, self.time))

            self.ret = self.helper.select_one('select count(*) from informaTable where stu_num={}'.format(self.stunum))
            print("rec", self.ret)
            if self.ret[0] > 0:
                QMessageBox.critical(self, 'Wrong', '该学号已经存在!')
            else:
                # 插入卡号到数据库中
                self.tableWidget.insertRow(self.rowcount)  # 在末尾插入一行
                self.tableWidget.setItem(self.rowcount, 0, QTableWidgetItem(self.stunum))  # 学号
                self.tableWidget.setItem(self.rowcount, 1, QTableWidgetItem(self.stuname))  # 姓名
                self.tableWidget.setItem(self.rowcount, 2, QTableWidgetItem(self.stuclass))  # 班级
                self.tableWidget.setCellWidget(self.rowcount, 3, self.face_pic)  # 人脸数据
                # self.tableWidget.setItem(self.rowcount, 3, QTableWidgetItem("人脸"))  # 人脸数据
                self.tableWidget.setItem(self.rowcount, 4, QTableWidgetItem(self.ID))  # 显示id
                self.tableWidget.setItem(self.rowcount, 5, QTableWidgetItem(self.usename))  # 显示操作者
                self.tableWidget.setItem(self.rowcount, 6, QTableWidgetItem(self.time))  # 显示时间
                QApplication.processEvents()  # 刷新表单数据

                self.helper.insert('insert into informaTable(stu_num,stu_name,stu_class,stu_info,stu_id,add_time,'
                                   'administrator) values(%s,%s,%s,%s,%s,%s,%s)', [self.stunum,
                                                                                   self.stuname,
                                                                                   self.stuclass,
                                                                                   self.stu_info,
                                                                                   self.ID,
                                                                                   self.time,
                                                                                   self.usename])
        except Exception as ex:
            print("卡号插入异常! 位置:MyMainWindow->seekID! 异常信息:{}".format(ex))

    def identifyID(self):
        try:
            self.image = self.helper.readImage("select stu_info from informaTable limit 1")
            # print(self.image)
            fout = open('face.png', 'wb')
            fout.write(self.image)
            fout.close()
            self._faceComparison()
        except Exception as ex:
            print("图片保存异常! 位置:MyMainWindow->identifyID 异常信息->{}".format(ex))

    # 人脸比对
    def _faceComparison(self):
        try:
            with open("../ui/image.png", 'rb') as f:
                facef = f.read()
            with open("../ui/face.png", 'rb') as f:
                faces = f.read()
            self.face = Face(facef=facef, faces=faces)
            self.face.get_img()
            self.face.result()
        except Exception as ex:
            print("人脸比对异常! 位置:MyMainWindow->_faceComparison 异常信息:{}".format(ex))

    def delID(self):
        try:
            print("删除学号")
            self.delids = self.priceArea_3.toPlainText()
            print("要删除的学号是:", self.delids)
            self.helper.delete('delete from informaTable where stu_num="{}"'.format(self.delids))
            print("已删除学号{}".format(self.delids))

            item = self.tableWidget.findItems(self.delids, QtCore.Qt.MatchExactly)  # 遍历表格查找具体单元格
            row = item[0].row()  # 获取数据所在的行号
            print(row)
            self.tableWidget.removeRow(row)  # 删除对应数据所在的行
            QApplication.processEvents()  # 刷新表单数据
        except Exception as ex:
            print("删除数据异常! 位置:MyMainWindow->delID 异常信息:{}".format(ex))

    def showform(self, usename):
        print("show")
        self.usename = usename
        self.form3.show()


# 多线程读取文件
class ReadFace(QThread):
    readSin = pyqtSignal(object)

    def __init__(self, parent=None):
        super(QThread, self).__init__(parent)
        self.runRead = 0  # 控制线程

    def run(self):
        try:
            while True:
                if self.runRead:
                    print("读取文件!")
                    fb = open('../faceID/img/ScreeFace.png', 'rb')
                    self.face = fb.read()
                    fb.close()
                    self.readSin.emit(self.face)
                    self.runRead = 0
        except Exception as ex:
            print("读取文件异常! 位置:ReadFace->run 异常信息:{}".format(ex))


# 多线程查询数据
class showMainWindos(QThread):
    showSin = pyqtSignal(object)  # 显示线程信号

    def __init__(self, parent=None):
        super(QThread, self).__init__(parent)
        self.runShow = 0
        self.helper = MysqlHelper(host='120.24.222.48', database='informatioBase', user='root',
                                  password='root')  # 链接数据库

    def run(self):
        try:
            print("进入查询线程")
            while True:
                if self.runShow:
                    self.select_all = self.helper.select_all('select * from informaTable')
                    self.showSin.emit(self.select_all)
                    self.runShow = 0
        except Exception as ex:
            print("查询数据库线程异常! 位置:showMainWindos->run 异常信息:{}".format(ex))


# 多线程读取卡号
class ReadID(QThread):
    _sinid = pyqtSignal()

    def __init__(self, parent=None):
        super(QThread, self).__init__(parent)
        try:
            self.ser = self.ser = serial.Serial("com13", 115200, timeout=0.5)
        except Exception as ex:
            print("串口异常! 位置:ReadID->__init__ 异常信息:{}".format(ex))

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
            print("读取卡号异常! 位置:ReadID->rec 异常信息->{}".format(ex))

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
            print("解码异常! 位置:ReadID->run 异常信息->{}".format(ex))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.showform()
    # window.show()
    sys.exit(app.exec_())
