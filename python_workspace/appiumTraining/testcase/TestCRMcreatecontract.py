# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower
from testcase.TestCRM import TestCRM


class TestCRMcreatecontract(TestCRM):

    #  创建合同
    def createcontract(self):

        # 点击合同图标
        self.driver.click("text= 合同 ")
        # 点击添加合同按钮
        self.driver.click("text=sYVInwAAAABJRU5ErkJggg==")
        #选择来源客户
        self.driver.click("text=来源客户*")
        self.driver.click("text=crm000001")
        #合同审批人
        self.driver.click("text=合同审批人*")
        self.driver.click("text=办公室")
        #合同金额
        self.driver.send_keys("xpath=//*[@text=\"请输入\"][1]", "100")
        sleep(4)
        #合同生效日期
        self.driver.click("text=合同生效时间*")
        self.driver.click("text=确定")
        sleep(5)

        #保存
        self.driver.click("text=保存")
        #返回
        self.driver.click_index("class=android.view.View",1)
        sleep(5)


    def test_weiChat(self):
        self.login()
        self.createcontract()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
