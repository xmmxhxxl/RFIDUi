# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from ui.Login_pan import Ui_Form
from windows.MysqlHelper import MysqlHelper
from ui.regist_pan import Registpane


class LoginPane(QWidget, Ui_Form):
    show_register_pane_signal = pyqtSignal()
    show_login_in_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(LoginPane, self).__init__(parent)
        self.form2 = QtWidgets.QWidget()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
        self.btn_regist.clicked.connect(self.sign_in)

    def sign_in(self):
        print('page to regist')
        self.registapane = Registpane()
        self.registapane.showwindo()
        # self.registapane.register()

    # 登录
    def login(self):
        self.name = self.ed_name.text()
        # print("登陆用户为：", self.name)
        pwd = self.ed_pwd.text()
        if self.name == '':
            QMessageBox.critical(self, 'Wrong', '请输入账号!')
        else:
            # 连接对象
            helper = MysqlHelper(host='localhost', database='demomysql', user='root', password='root')
            # 执行sql语句
            ret = helper.select_one('select count(*) from demotable where user_name=%s and user_pwd=%s',
                                         [self.name, helper.my_md5(pwd)])
            print(ret)
        if ret[0] > 0:
            # QMessageBox.information(self, 'Information', '登录成功!')
            # self.show_login_in_signal.emit()
            print('登录成功！')
            from ui.mainWindos import MyMainWindow
            ui = MyMainWindow()
            ui.show()
        else:
            QMessageBox.critical(self, 'Wrong', '帐号密码错误!')
            print('登录失败，请重新登录！')

        # self.ed_name.clear()
        self.ed_pwd.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
