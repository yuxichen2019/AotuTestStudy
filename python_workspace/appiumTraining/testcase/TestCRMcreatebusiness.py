# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower
from testcase.TestCRM import TestCRM


class TestCRMcreatebusiness(TestCRM):

    #  创建商机
    def createbusiness(self):

        # 点击商机图标
        self.driver.click("text= 商机 ")
        # 点击添加商机按钮
        self.driver.click("text=sYVInwAAAABJRU5ErkJggg==")
        #选择客户名称
        self.driver.click("xpath=//*[@text=\"请选择\"][1]")
        self.driver.click("text=crm000001")
        #商机状态组
        self.driver.click_index("class=android.widget.Spinner",0)
        self.driver.click("text=默认分组")

        #商机进度
        self.driver.click_index("class=android.widget.Spinner",1)
        self.driver.click("text=初步洽谈")
        sleep(5)
        #产品
        self.driver.click("text=产品")
        self.driver.click_index("class=android.widget.Image",2)
        self.driver.click("text=确定")
        self.driver.click("text=确定")
        sleep(5)
        #保存
        self.driver.click("text=保存")
        #返回
        self.driver.click_index("class=android.view.View",1)
        sleep(5)


    def test_weiChat(self):
        self.login()
        self.createbusiness()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
