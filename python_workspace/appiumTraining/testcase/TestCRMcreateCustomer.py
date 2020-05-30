# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower
from testcase.TestCRM import TestCRM


class TestCRMcreateCustomer(TestCRM):

    #  创建客户
    def createCustomer(self):

        # 点击客户图标
        self.driver.click("text= 客户 ")
        # 点击添加客户按钮
        self.driver.click("text=sYVInwAAAABJRU5ErkJggg==")
        #输入客户名称
        self.driver.send_keys("xpath=//*[@text=\"请输入\"][1]","crm000001")

        #输入客户编号
        self.driver.send_keys("xpath=//*[@text=\"请输入\"][1]","c000001")
        #选择客户信息来源
        self.driver.click_index("class=android.view.View",59)
        self.driver.click("text=电话营销")
        #保存
        self.driver.click("text=保存")
        #点击返回
        self.driver.click_index("class=android.view.View",10)
        # sleep(5)
        # # # 向上滑动屏幕
        # # self.driver.swipe_up(n=3)

    def test_weiChat(self):
        self.login()
        self.createCustomer()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
