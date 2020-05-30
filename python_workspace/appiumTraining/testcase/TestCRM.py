# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower


class TestCRM(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 模拟器
        # self.driver = SunFlower("192.168.136.101:5555", "5.1",
        #                         "com.wukong.crm",
        #                         "com.wukong.crm.MainActivity")
        # 三星手机
        self.driver = SunFlower("8FS7N16422000903", "7.0",
                                "com.jianxin.crm",
                                "com.jianxin.crm.MainAppActivity")

        # self.driver = SunFlower("GWY0217805012421", "8.0.0",
        #                         "com.jianxin.crm",
        #                         "com.jianxin.crm.MainAppActivity")
        # self.driver.switch_to_webViewOrNative()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 登录CRM系统
    def login(self):
        # 点击登录按钮
        self.driver.click("text=登录")
        # 输入用户名
        self.driver.send_keys("text=请输入账号", "13316998731")
        # 输入密码
        self.driver.send_keys("text=请输入密码", "yuan2019")
        # 点击登录
        self.driver.click("text=登录")
    # 退出CRM系统
    def logout(self):
        # 点击我的标签
        self.driver.click("text=我的")
        # 点击设置按钮
        self.driver.click("text=设置")
        # 点击退出
        # self.driver.click("text=退出 ")
        # self.driver.click("xpath=//android.widget.Button[@text=\"退出 \"]")
        self.driver.click("xpath=//android.widget.Button[contains(@text,\"退出 \")]")
        sleep(5)

    #  创建客户
    def createCustomer(self):
        # 点击CRM标签
        self.driver.click("xpath=//span[contains(text(),'CRM')]")
        # 点击客户图标
        self.driver.click("xpath=//p[contains(text(),'客户')]")
        # 点击添加客户按钮
        self.driver.click("xpath=//*[@id='app']/div[1]/div[1]/div[3]/span/img")
        # 向上滑动屏幕
        self.driver.swipe_up(n=3)

    # def test_weiChat(self):
    #     self.login()
    #     # self.createCustomer()
    #     self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
