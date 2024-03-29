# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 706)
        Form.setStyleSheet("    /*background-color:rgb(220, 220, 220);")
        self.price_2 = QtWidgets.QLabel(Form)
        self.price_2.setEnabled(True)
        self.price_2.setGeometry(QtCore.QRect(10, 170, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_2.setFont(font)
        self.price_2.setObjectName("price_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 941, 481))
        self.tableWidget.setStyleSheet("    border-radius: 10px;  \n"
"     border: 0px groove white;\n"
"    font: 10pt \"宋体\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.price_3 = QtWidgets.QLabel(Form)
        self.price_3.setEnabled(True)
        self.price_3.setGeometry(QtCore.QRect(10, 90, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_3.setFont(font)
        self.price_3.setObjectName("price_3")
        self.priceArea_3 = QtWidgets.QTextEdit(Form)
        self.priceArea_3.setGeometry(QtCore.QRect(10, 120, 211, 41))
        self.priceArea_3.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 14pt \"宋体\";")
        self.priceArea_3.setObjectName("priceArea_3")
        self.stu_num = QtWidgets.QTextEdit(Form)
        self.stu_num.setGeometry(QtCore.QRect(10, 40, 161, 41))
        self.stu_num.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 14pt \"宋体\";")
        self.stu_num.setObjectName("stu_num")
        self.name = QtWidgets.QTextEdit(Form)
        self.name.setGeometry(QtCore.QRect(180, 40, 131, 41))
        self.name.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 14pt \"宋体\";")
        self.name.setObjectName("name")
        self.classes = QtWidgets.QTextEdit(Form)
        self.classes.setGeometry(QtCore.QRect(320, 40, 161, 41))
        self.classes.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 14pt \"宋体\";")
        self.classes.setObjectName("classes")
        self.stu_numtext = QtWidgets.QLabel(Form)
        self.stu_numtext.setEnabled(True)
        self.stu_numtext.setGeometry(QtCore.QRect(10, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stu_numtext.setFont(font)
        self.stu_numtext.setObjectName("stu_numtext")
        self.name_text = QtWidgets.QLabel(Form)
        self.name_text.setEnabled(True)
        self.name_text.setGeometry(QtCore.QRect(190, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name_text.setFont(font)
        self.name_text.setObjectName("name_text")
        self.class_text = QtWidgets.QLabel(Form)
        self.class_text.setEnabled(True)
        self.class_text.setGeometry(QtCore.QRect(330, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.class_text.setFont(font)
        self.class_text.setObjectName("class_text")
        self.sut_id = QtWidgets.QTextEdit(Form)
        self.sut_id.setGeometry(QtCore.QRect(490, 40, 141, 41))
        self.sut_id.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 14pt \"宋体\";")
        self.sut_id.setObjectName("sut_id")
        self.price = QtWidgets.QLabel(Form)
        self.price.setEnabled(True)
        self.price.setGeometry(QtCore.QRect(490, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.price_4 = QtWidgets.QLabel(Form)
        self.price_4.setEnabled(True)
        self.price_4.setGeometry(QtCore.QRect(640, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_4.setFont(font)
        self.price_4.setObjectName("price_4")
        self.openface_but = QtWidgets.QPushButton(Form)
        self.openface_but.setGeometry(QtCore.QRect(640, 40, 141, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.openface_but.sizePolicy().hasHeightForWidth())
        self.openface_but.setSizePolicy(sizePolicy)
        self.openface_but.setMinimumSize(QtCore.QSize(0, 0))
        self.openface_but.setMaximumSize(QtCore.QSize(150, 40))
        self.openface_but.setStyleSheet("    /*border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);\n"
"*/\n"
"QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    color:white;\n"
"    background-color:rgb(79, 125, 163);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(127, 161, 190);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.openface_but.setToolTip("打开文件")
        self.openface_but.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/open_fw.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.openface_but.setIcon(icon)
        self.openface_but.setObjectName("openface_but")
        self.confirm_but = QtWidgets.QPushButton(Form)
        self.confirm_but.setGeometry(QtCore.QRect(840, 40, 111, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_but.sizePolicy().hasHeightForWidth())
        self.confirm_but.setSizePolicy(sizePolicy)
        self.confirm_but.setMaximumSize(QtCore.QSize(150, 40))
        self.confirm_but.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    color:white;\n"
"    background-color:rgb(79, 125, 163);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(127, 161, 190);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.confirm_but.setToolTip("请确认信息无误!")
        self.confirm_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/quren.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.confirm_but.setIcon(icon1)
        self.confirm_but.setObjectName("confirm_but")
        self.renovate_but = QtWidgets.QPushButton(Form)
        self.renovate_but.setGeometry(QtCore.QRect(140, 170, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.renovate_but.sizePolicy().hasHeightForWidth())
        self.renovate_but.setSizePolicy(sizePolicy)
        self.renovate_but.setMinimumSize(QtCore.QSize(0, 0))
        self.renovate_but.setMaximumSize(QtCore.QSize(150, 40))
        self.renovate_but.setStyleSheet("    /*border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);\n"
"*/\n"
"QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    color:white;\n"
"    background-color:rgb(79, 125, 163);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(127, 161, 190);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.renovate_but.setToolTip("刷新")
        self.renovate_but.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/refresh_w.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.renovate_but.setIcon(icon2)
        self.renovate_but.setObjectName("renovate_but")
        self.del_but = QtWidgets.QPushButton(Form)
        self.del_but.setGeometry(QtCore.QRect(840, 120, 111, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_but.sizePolicy().hasHeightForWidth())
        self.del_but.setSizePolicy(sizePolicy)
        self.del_but.setMaximumSize(QtCore.QSize(150, 40))
        self.del_but.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    color:white;\n"
"    background-color:rgb(79, 125, 163);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(127, 161, 190);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.del_but.setToolTip("删除后不可撤销!")
        self.del_but.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/del_w.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.del_but.setIcon(icon3)
        self.del_but.setObjectName("del_but")

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.stu_num, self.name)
        Form.setTabOrder(self.name, self.classes)
        Form.setTabOrder(self.classes, self.confirm_but)
        Form.setTabOrder(self.confirm_but, self.priceArea_3)
        Form.setTabOrder(self.priceArea_3, self.renovate_but)
        Form.setTabOrder(self.renovate_but, self.tableWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.price_2.setText(_translate("Form", "已添加的卡号"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "班级"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "人脸数据"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "卡号"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "管理员"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "时间"))
        self.price_3.setText(_translate("Form", "删除"))
        self.stu_numtext.setText(_translate("Form", "学号"))
        self.name_text.setText(_translate("Form", "姓名"))
        self.class_text.setText(_translate("Form", "班级"))
        self.price.setText(_translate("Form", "卡号"))
        self.price_4.setText(_translate("Form", "人脸数据"))
import ui.image_rc
