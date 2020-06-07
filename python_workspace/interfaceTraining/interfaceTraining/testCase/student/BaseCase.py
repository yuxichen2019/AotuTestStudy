import logging
import os
import unittest

from framework.BlueRose import BlueRose


class BaseCase(unittest.TestCase):
    dataPath =''
    def setUp(self):
        self.requests = BlueRose()
        self.logger = self.requests.logger
        self.baseURL = "http://localhost:8888"
        self.logger.info("Test case execute begin")

    def tearDown(self):
        self.logger.info("Test case execute end")



    # 获取刷新Token
    # def refreshPhpSessId(self):
    #     # 登录的url地址
    #     url = self.baseURL + "/login"
    #     # 发送请求
    #     response = self.requests.sendRequests(url=url, method="get")
    #     # 获取cookie的值
    #     phpsessid = self.requests.getCookiesValue(response, "PHPSESSID")
    #     self.logger.info("phpsessid is："+phpsessid)
    #     return phpsessid


    # 登陆
    def login(self, username, password):
        # 登录url地址
        url = self.baseURL + "/login"
        # 请求参数
        data = {"name": username, "password": password, "config_id": ""}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "utf-8"}
        # 响应报文
        response = self.requests.sendRequests(url=url, method="post", data=data, headers=header)
        # 获取响应的结果
        result = self.requests.getJsonFilesValue(response, "info")
        # 断言结果
        self.assertEqual(result, "登录成功")


