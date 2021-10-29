# -*- codeing = utf-8 -*-
# @Time : 2021/10/29 14:22
# @Author : liman
# @File : serialProject.py
# @Software : PyCharm
import serial
from time import sleep


class SerialRead():

    def __init__(self, com, bits):
        self.com = com
        self.bits = bits
        self.ser = serial.Serial(self.com, self.bits, timeout=0.5)

    def rec(self, ser):
        while True:
            data = ser.read_all().decode()
            if data == '':
                continue
            else:
                break
                sleep(0.02)
        return data

    def read(self):
        # ser = serial.Serial('com13', 115200, timeout=0.5)
        if self.ser.isOpen():
            print("open")
        else:
            print("not")

        while True:
            data = self.rec(self.ser)
            if data != b'':
                print("data:", data)
                print("解码", data.encode().hex())
                if data == b'x':
                    print("exit")
                    break
        return data
