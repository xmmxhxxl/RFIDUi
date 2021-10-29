# -*- codeing = utf-8 -*-
# @Time : 2021/10/29 13:33
# @Author : liman
# @File : testser.py
# @Software : PyCharm
import serial
from time import sleep


def rec(serial):
    while True:
        data = serial.read_all().decode()
        if data == '':
            continue
        else:
            break
            sleep(0.02)
    return data


if __name__ == '__main__':
    serial = serial.Serial('com13', 115200, timeout=0.5)
    if serial.isOpen():
        print("open")
    else:
        print("not")

    while True:
        data = rec(serial)
        if data != b'':
            print("data:", data)
            print("解码", data.encode().hex())
            if data == b'x':
                print("exit")
                break
