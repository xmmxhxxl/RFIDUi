# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 531)
        Form.setStyleSheet("    /*background-color:rgb(220, 220, 220);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(12, 22, 441, 491))
        self.label.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.priceButton_2 = QtWidgets.QPushButton(Form)
        self.priceButton_2.setGeometry(QtCore.QRect(570, 430, 191, 61))
        self.priceButton_2.setStyleSheet("QPushButton\n"
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
        self.priceButton_2.setToolTip("单击确认,双击提交!")
        self.priceButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/quren.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.priceButton_2.setIcon(icon)
        self.priceButton_2.setObjectName("priceButton_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(480, 30, 371, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.price_2 = QtWidgets.QLabel(self.widget)
        self.price_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_2.setFont(font)
        self.price_2.setObjectName("price_2")
        self.horizontalLayout.addWidget(self.price_2)
        self.stu_num = QtWidgets.QTextEdit(self.widget)
        self.stu_num.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 17pt \"宋体\";")
        self.stu_num.setObjectName("stu_num")
        self.horizontalLayout.addWidget(self.stu_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.price_3 = QtWidgets.QLabel(self.widget)
        self.price_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_3.setFont(font)
        self.price_3.setObjectName("price_3")
        self.horizontalLayout_2.addWidget(self.price_3)
        self.stu_name = QtWidgets.QTextEdit(self.widget)
        self.stu_name.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 17pt \"宋体\";")
        self.stu_name.setObjectName("stu_name")
        self.horizontalLayout_2.addWidget(self.stu_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.price_4 = QtWidgets.QLabel(self.widget)
        self.price_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_4.setFont(font)
        self.price_4.setObjectName("price_4")
        self.horizontalLayout_3.addWidget(self.price_4)
        self.stu_class = QtWidgets.QTextEdit(self.widget)
        self.stu_class.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 17pt \"宋体\";")
        self.stu_class.setObjectName("stu_class")
        self.horizontalLayout_3.addWidget(self.stu_class)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.price_5 = QtWidgets.QLabel(self.widget)
        self.price_5.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_5.setFont(font)
        self.price_5.setObjectName("price_5")
        self.horizontalLayout_4.addWidget(self.price_5)
        self.stu_id = QtWidgets.QTextEdit(self.widget)
        self.stu_id.setStyleSheet("    border-radius: 10px;  \n"
"     border: 2px groove white;\n"
"    font: 17pt \"宋体\";")
        self.stu_id.setObjectName("stu_id")
        self.horizontalLayout_4.addWidget(self.stu_id)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.price_2.setText(_translate("Form", "学号"))
        self.price_3.setText(_translate("Form", "姓名"))
        self.price_4.setText(_translate("Form", "班级"))
        self.price_5.setText(_translate("Form", "卡号"))
import ui.image_rc
