# -*- coding: utf-8 -*- 
# 2020/5/30 14:54 
# appiumTraining
# BaseCase.py 
# company


import unittest
from framework.SunFlower import SunFlower



class BaseCase(unittest.TestCase):

    #@classmethod
    def setUp(self):
        self.driver = SunFlower("K6T6R17124002359", "7", "com.tencent.mm",
                                "com.tencent.mm.ui.LauncherUI")

        self.login()


    #@classmethod
    def tearDown(self):
        self.logout()
        self.driver.quit()

    # 登录微信
    def login(self):
        #切换验证方式
        #self.driver.click("id=com.tencent.mm:id/cqq")
        #用密码登录
        #self.driver.click("id=com.tencent.mm:id/l_")
        # 输入密码
        self.driver.send_keys("id=com.tencent.mm:id/bfl", "yb092226")
        # 点击登录
        self.driver.click("id=com.tencent.mm:id/d2y")


    # 退出微信登录
    def logout(self):
        # 点击返回
        self.driver.click("des=返回")
        # 点击返回
        self.driver.click("text=取消")
        # 点击我标签
        self.driver.click("text=我")
        # 点击设置
        self.driver.click("text=设置")
        # 向上滑动屏幕
        #self.driver.swipe_up(n=2)
        # 点击退出
        self.driver.click("text=退出")
        # 点击退出登录
        # self.driver.click("text=退出登录")
        # 点击退出
        self.driver.click("text=退出登录")
        self.driver.click("text=退出")





