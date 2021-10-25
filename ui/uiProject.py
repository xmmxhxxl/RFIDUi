# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 481)
        Form.setStyleSheet("    /*background-color:rgb(220, 220, 220);")
        self.price = QtWidgets.QLabel(Form)
        self.price.setEnabled(True)
        self.price.setGeometry(QtCore.QRect(10, 10, 121, 24))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.priceArea_2 = QtWidgets.QTextEdit(Form)
        self.priceArea_2.setGeometry(QtCore.QRect(10, 40, 301, 41))
        self.priceArea_2.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 10pt \"宋体\";")
        self.priceArea_2.setPlaceholderText("手动输入或自动识别卡号")
        self.priceArea_2.setObjectName("priceArea_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 40, 231, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.priceButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.priceButton_3.sizePolicy().hasHeightForWidth())
        self.priceButton_3.setSizePolicy(sizePolicy)
        self.priceButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.priceButton_3.setMaximumSize(QtCore.QSize(150, 40))
        self.priceButton_3.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);\n"
"")
        self.priceButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/ind.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.priceButton_3.setIcon(icon)
        self.priceButton_3.setObjectName("priceButton_3")
        self.horizontalLayout.addWidget(self.priceButton_3)
        self.priceButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceButton_2.sizePolicy().hasHeightForWidth())
        self.priceButton_2.setSizePolicy(sizePolicy)
        self.priceButton_2.setMaximumSize(QtCore.QSize(150, 40))
        self.priceButton_2.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);")
        self.priceButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/arc.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.priceButton_2.setIcon(icon1)
        self.priceButton_2.setObjectName("priceButton_2")
        self.horizontalLayout.addWidget(self.priceButton_2)
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 541, 261))
        self.tableWidget.setStyleSheet("    border-radius: 10px;  \n"
"     border: 0px groove white;\n"
"    font: 10pt \"宋体\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
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
        self.priceArea_3.setGeometry(QtCore.QRect(10, 120, 301, 41))
        self.priceArea_3.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 10pt \"宋体\";")
        self.priceArea_3.setPlaceholderText("手动输入或自动识别卡号")
        self.priceArea_3.setObjectName("priceArea_3")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(320, 120, 231, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.priceButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.priceButton_4.sizePolicy().hasHeightForWidth())
        self.priceButton_4.setSizePolicy(sizePolicy)
        self.priceButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.priceButton_4.setMaximumSize(QtCore.QSize(150, 40))
        self.priceButton_4.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);\n"
"")
        self.priceButton_4.setText("")
        self.priceButton_4.setIcon(icon)
        self.priceButton_4.setObjectName("priceButton_4")
        self.horizontalLayout_2.addWidget(self.priceButton_4)
        self.priceButton_5 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceButton_5.sizePolicy().hasHeightForWidth())
        self.priceButton_5.setSizePolicy(sizePolicy)
        self.priceButton_5.setMaximumSize(QtCore.QSize(150, 40))
        self.priceButton_5.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    background-color:rgb(229, 229, 229);")
        self.priceButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/del.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.priceButton_5.setIcon(icon2)
        self.priceButton_5.setObjectName("priceButton_5")
        self.horizontalLayout_2.addWidget(self.priceButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.price.setText(_translate("Form", "卡号"))
        self.price_2.setText(_translate("Form", "已添加的卡号"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "卡号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "管理员"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "时间"))
        self.price_3.setText(_translate("Form", "删除"))
import ui.image_rc
