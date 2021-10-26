# -*- codeing = utf-8 -*-
# @Time : 2021/10/26 21:49
# @Author : liman
# @File : demomyql.py
# @Software : PyCharm
import pymysql
import hashlib
her = pymysql.connect(host='120.24.222.48',database='informationBase',user='root',password='root',port=3306)
cur = her.cursor()
cur.execute('select * from informaTable')
result = cur.fetchall()

print(result)