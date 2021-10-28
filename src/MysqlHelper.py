# -*- coding: utf-8 -*-
import sys

import pymysql
import hashlib
import time


class MysqlHelper():
    def __init__(self, host, database, user, password, port=3306, charset='utf8'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset

    # 连接对象
    def connect(self):
        self.conn = pymysql.connect(host=self.host, database=self.database, user=self.user, password=self.password,
                                    port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    # 关闭
    def close(self):
        self.cursor.close()
        self.conn.close()

    def newNserTable(self, usetable):
        sql = '''
            create table table{}(
                frequency int(32) primary key auto_increment,
                label varchar(255),
                similarity varchar(255),
                price float(16),
                date timestamp(6),
                total float(16)
            );
        '''.format(usetable)

        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print("数据表创建失败{}".format(usetable), e)

    def insterImgae(self, sql, image):
        try:
            self.connect()
            self.cursor.execute(sql, image)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except Exception as ex:
            print("人脸数据插入异常！", ex)

    def readImage(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            # fout = open('image.png', 'wb')
            # fout.write(self.cursor.fetchone()[0])
            # fout.close()
            self.image = self.cursor.fetchone()[0]
            self.cursor.close()
            self.conn.close()
        except IOError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        return self.image

    # 查询一条数据
    def select_one(self, sql, params=[]):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as ex:
            print(ex)
        return result

    # 查询所有数据
    def select_all(self, sql):
        result = ''
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
        except Exception as ex:
            print(ex)
        return result

    # 增删改代码的封装
    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as ex:
            print(ex)
        return count

    def __editdata(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as ex:
            print(ex)
        return count

    # 增
    def insert(self, sql, params=[]):
        return self.__edit(sql, params)

    # 插入数据
    def insertdata(self, sql):
        return self.__editdata(sql)

    # 改
    def update(self, sql, params=[]):
        return self.__edit(sql, params)

    # 删
    def delete(self, sql, params=[]):
        return self.__edit(sql, params)

    # 密码加密
    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()
