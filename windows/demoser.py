# -*- codeing = utf-8 -*-
# @Time : 2021/10/28 11:57
# @Author : liman
# @File : demoser.py
# @Software : PyCharm
import time
import serial
ser = serial.Serial(
    port='com8',
    baudrate='115200',
    # parity=serial.PARITY_ODD,
    # stopbits=serial.STOPBITS_TWO,
    # bytesize=serial.SEVENBITS
)
data = ''
while True:
    data = ser.readline()
    print(data)