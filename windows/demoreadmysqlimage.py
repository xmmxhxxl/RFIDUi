# -*- codeing = utf-8 -*-
# @Time : 2021/10/28 12:21
# @Author : liman
# @File : demoreadmysqlimage.py
# @Software : PyCharm
import pymysql
import sys

try:
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='root', db='demomysql')
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM image LIMIT 1")
    fout = open('image.png', 'wb')
    fout.write(cursor.fetchone()[0])
    fout.close()
    cursor.close()
    conn.close()

except IOError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
