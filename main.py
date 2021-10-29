from ui.useInterface import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class usein(QWidget, Ui_Form):

    def __init__(self):
        super(usein, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = usein()
    window.show()
    sys.exit(app.exec_())
