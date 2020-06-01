# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower
from testcase.TestCRM import TestCRM


class TestCRMcreateCustomer(TestCRM):

    #  创建线索
    def createClue(self):

        # 点击线索图标
        self.driver.click("text= 线索 ")
        # 点击添加线索按钮
        self.driver.click("text=sYVInwAAAABJRU5ErkJggg==")
        #输入联系人姓名
        self.driver.send_keys("xpath=//*[@text=\"请输入\"][1]","LXR000003")
        #保存
        self.driver.click("text=保存")
        #返回
        self.driver.click_index("class=android.view.View",1)
        sleep(5)


    def test_weiChat(self):
        self.login()
        self.createClue()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
