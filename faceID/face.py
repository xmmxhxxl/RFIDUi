# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 16:23
# @Author : liman
# @File : face.py
# @Software : PyCharm
import requests
from aip import AipFace
import json
import os
import numpy as np
import matplotlib
import base64


class Face():

    def __init__(self):
        super().__init__()
        self.APP_ID = '25065352'
        self.APP_KEY = 'gDjVAHz8CkxIvvh4Dii1Nb7C'
        self.SK = 'dVdid50k3xNylRLDh5SsM7zsn0gNV2Pm'
        self.bas = 'BASE64'
        self.client = AipFace(self.APP_ID, self.APP_KEY, self.SK)

    def get_img(self):
        # 1.读取两张图片数据，整合两张图片 json数据
        with open("../faceID/mysqlDownload/downloadFace.png", "rb") as f:
            pic1 = f.read()
            # print(pic1)
        with open("../faceID/ScreeFace/ScreeFace.png", "rb") as f:
            pic2 = f.read()
            # print(base64.b64encode(pic1))
        self.image_data = json.dumps([
            {"image": str(base64.b64encode(pic1), "utf-8"), "image_type": "BASE64"},
            {"image": str(base64.b64encode(pic2), "utf-8"), "image_type": "BASE64"}
        ])
        print(self.image_data)
    def result(self):
        # 2.拼接人脸识别API接口
        get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(
            self.APP_KEY, self.SK)

        API_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="

        text = requests.get(get_token).json()
        print(text['access_token'])

        url = API_url + text['access_token']
        print(url)
        # 3.请求API接口传入json数据，返回图片相似度
        self.response = requests.post(url, self.image_data).json()

        print(self.response)

        score = self.response['result']['score']
        error_code = self.response['error_code']
        print("相似度为：{}%".format(score))
        print("错误码为", error_code, type(error_code))

    # def face_add(self, gropid, groplist):
    #     image = './img1.jpg'
    #     result = self.client.addUser(image, 'BASE64', gropid, groplist)
    #     if result['error_code'] == "0":
    #         print("增加成功")
    #     else:
    #         print("增加失败")


if __name__ == '__main__':
    face_score = Face()
    face_score.get_img()
    face_score.result()
