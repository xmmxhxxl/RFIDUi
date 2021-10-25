# -*- coding: utf-8 -*-

from PyQt5.Qt import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from windows.MysqlHelper import MysqlHelper
from ui.Regist_pane import Ui_Form


class Registpane(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.form2 = QtWidgets.QWidget()
        self.setupUi(self.form2)
        self.btn_regist.clicked.connect(self.register)
        self.btn_exit.clicked.connect(self.exit_func)

    # 注册
    def register(self):
        name = self.ed_name.text()
        pwd = self.ed_pwd.text()
        pwd2 = self.ed_pwd_2.text()

        if name == '':
            QMessageBox.critical(self, 'Wrong', '请输入账号!')
        else:
            # 连接对象
            helper = MysqlHelper(host='localhost', database='demomysql', user='root', password='root')
            # # 执行sql语句
            ret1 = helper.select_one('select count(*) from demotable where user_name=%s ', name)
            print(ret1)
            # print(ret1)
            if ret1[0] > 0:
                QMessageBox.critical(self, 'Wrong', '该账号已被注册!')
            else:
                if (pwd == pwd2):
                    # 连接对象
                    helper = MysqlHelper(host='localhost', database='demomysql', user='root', password='root')
                    # 执行sql语句
                    self.ret2 = helper.insert('insert into demotable(user_name, user_pwd) values(%s,%s)',
                                              [name, helper.my_md5(pwd)])
                    helper.newNserTable(name)
                    print("re2:", self.ret2)
                else:
                    QMessageBox.critical(self, 'Wrong', '输入的密码不一致!')

        try:
            if self.ret2 > 0:
                print("re2 is:", self.ret2)
                QMessageBox.information(self, 'Information', '注册成功！')
                print('注册成功！')
            else:
                print("cuowu:", self.ret2)
                QMessageBox.critical(self, 'Wrong', '该用户已存在！')
                print('注册失败，请重新注册！')
        except Exception as e:
            print(e)
            print("用户已经被注册")

        self.ed_pwd.clear()
        self.ed_pwd_2.clear()
        self.ed_name.clear()

    def exit_func(self):
        print("regist-exit")

    def showwindo(self):
        print("show Registration interface")
        self.form2.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Registpane()
    window.show()
    sys.exit(app.exec_())
