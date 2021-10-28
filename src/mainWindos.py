# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 11:33
# @Author : liman
# @File : main.py
# @Software : PyCharm
import time

from PyQt5.QtGui import *
from PyQt5.uic.properties import QtWidgets
from ui.uiProject import Ui_Form
from PyQt5.Qt import *
from PyQt5 import QtWidgets, QtCore
from src.MysqlHelper import MysqlHelper


class MyMainWindow(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.form3 = QtWidgets.QWidget()
        self.setupUi(self.form3)
        # self.name = username
        self.priceButton_2.clicked.connect(self.seekID)  # 添加卡信号槽
        self.priceButton_5.clicked.connect(self.delID)  # 删除卡的信号槽
        self.priceButton_3.clicked.connect(self.identifyID)  # 自动查找卡号信号槽

        self.helper = MysqlHelper(host='120.24.222.48', database='informatioBase', user='root', password='root')
        self.showtable()

    def showtable(self):
        self.line = 0
        self.select_all = self.helper.select_all('select * from informaTable')
        # print("数据表的所有数据是:{}".format(self.select_all))
        for item in self.select_all:
            self.tableWidget.insertRow(self.line)
            self.tableWidget.setItem(self.line, 0, QTableWidgetItem(item[0]))
            self.tableWidget.setItem(self.line, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(self.line, 2, QTableWidgetItem(item[2]))
            # self.tableWidget.setItem(self.line, 3, QTableWidgetItem(item[3]))
            self.tableWidget.setItem(self.line, 4, QTableWidgetItem(item[4]))
            self.tableWidget.setItem(self.line, 5, QTableWidgetItem(item[5]))
            self.tableWidget.setItem(self.line, 6, QTableWidgetItem(item[6]))
        QApplication.processEvents()  # 刷新表单数据

    def seekID(self):
        print("识别卡号")
        self.ID = self.priceArea_2.toPlainText()  # 获取卡号
        self.stunum = self.stu_num.toPlainText()  # 获取学号
        self.stuname = self.name.toPlainText()  # 获取姓名
        self.stuclass = self.classes.toPlainText()  # 获取班级信息
        # fb = open("../faceID/img2.jpg", 'rb')  # 打开文件
        # self.stu_info = fb.read()  # 二进制读取人脸信息
        # fb.close()  # 关闭链接
        # self.stu_info = self.image
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化获取当前时间
        self.rowcount = self.tableWidget.rowCount()  # 获取当前表格的行数
        print(
            "姓名:{},学号:{},班级:{},卡号:{},管理员:{},时间:{}".format(self.stunum, self.stuname, self.stuclass,
                                                          self.ID,
                                                          self.usename, self.time))
        try:
            self.ret = self.helper.select_one('select count(*) from informaTable where stu_num={}'.format(self.stunum))
            print("rec", self.ret)
            if self.ret[0] > 0:
                QMessageBox.critical(self, 'Wrong', '该学号已经存在!')
            else:
                fb = open("../faceID/img2.jpg", 'rb')  # 打开文件
                self.stu_info = fb.read()  # 二进制读取人脸信息
                fb.close()  # 关闭链接
                # 插入卡号到数据库中
                self.tableWidget.insertRow(self.rowcount)  # 在末尾插入一行
                self.tableWidget.setItem(self.rowcount, 0, QTableWidgetItem(self.stunum))  # 学号
                self.tableWidget.setItem(self.rowcount, 1, QTableWidgetItem(self.stuname))  # 姓名
                self.tableWidget.setItem(self.rowcount, 2, QTableWidgetItem(self.stuclass))  # 班级
                # self.tableWidget.setItem(self.rowcount, 3, QTableWidgetItem(self.image))  # 人脸数据
                self.tableWidget.setItem(self.rowcount, 4, QTableWidgetItem(self.ID))  # 显示id
                self.tableWidget.setItem(self.rowcount, 5, QTableWidgetItem(self.usename))  # 显示操作者
                self.tableWidget.setItem(self.rowcount, 6, QTableWidgetItem(self.time))  # 显示时间
                QApplication.processEvents()  # 刷新表单数据
                # print(self.stu_info)
                self.helper.insert('insert into informaTable(stu_num,stu_name,stu_class,stu_info,stu_id,add_time,'
                                   'administrator) values(%s,%s,%s,%s,%s,%s,%s)', [self.stunum,
                                                                                self.stuname,
                                                                                self.stuclass,
                                                                                self.stu_info,
                                                                                self.ID,
                                                                                self.time,
                                                                                self.usename])
                # self.helper.insterImgae('insert into informaTable(stu_info) values(%s)', self.stu_info)
                # print("刷1新界面")
        except Exception as ex:
            print("卡号插入失败！", ex)

    def identifyID(self):
        # print("查找卡号")
        # self.ID = self.priceArea_2.toPlainText()
        # print("卡号是：", self.ID)
        self.image = self.helper.readImage("select informaTable from stu_info limit 1")
        fout = open('../fa1ceID/img/image.png', 'wb')
        fout.write(self.image)
        fout.close()

    def delID(self):
        print("删除卡号")
        self.delids = self.priceArea_3.toPlainText()
        print("要删除的卡号是:", self.delids)
        self.helper.delete('delete from informaTable where stu_num="{}"'.format(self.delids))
        print("已删除卡号{}".format(self.delids))
        try:
            item = self.tableWidget.findItems(self.delids, QtCore.Qt.MatchExactly)  # 遍历表格查找具体单元格
            row = item[0].row()  # 获取数据所在的行号
            print(row)
            self.tableWidget.removeRow(row)  # 删除对应数据所在的行
            QApplication.processEvents()  # 刷新表单数据
        except Exception as ex:
            print("删除数据异常！", ex)

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
