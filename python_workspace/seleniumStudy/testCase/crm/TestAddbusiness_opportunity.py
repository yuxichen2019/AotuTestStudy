# -*- coding: utf-8 -*- 
# 2020/04/18 17:16 
# seleniumStudy
# TestAddbusiness_opportunity.py 
# company

import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from framework.BlueRose import BlueRose
from parameterized import parameterized
import datetime
from testCase.crm.BaseCase import BaseCase

#123

class TestAddBusinessOpportunity(BaseCase):

    # 新增商机
    @parameterized.expand([
        ("测试客户1")
        ])
    def test_add_business_opportunity(self,customername):
        #
        #点击商机管理
        self.driver.click("xpath=//span[text()='商机管理']")
        #点击商机
        self.driver.click("id=business-index")
        #新建商机
        self.driver.click('xpath=//a[@class="btn btn-primary btn-sm pull-left"]')
        #点击选择客户
        self.driver.click('id=customer_name')
        #输入目标客户
        self.driver.send_keys('id=search',customername)
        #点击搜索
        self.driver.click("xpath=//button[text()='立即搜索']")
        sleep(1)
        #点击目标客户
        self.driver.click('xpath=//td[text()="测试客户1"]')
        #点击选择客户框的确定
        self.driver.click_index('xpath=//span[text()="确认"]',0)
        # self.driver.click("xpath=(//span[text()='确认'])[1]")

        # 选择商机进度
        self.driver.click('xpath=//option[text()="完成收款"]')
        #时间-1-input的时间控件
        self.driver.send_keys("xpath=//input[@input_type='time']",'2020-04-28 16:28')
        #保存商机
        self.driver.click('id=save_submit')

        # alert = self.driver.find_element('xpath=//*[@id="toast-container"]/div/div[2]')
        # #print(alert.text)
        # assert alert.text == '添加客户成功'



if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddBusinessOpportunity)
    runer = HTMLTestRunner(title="简信CRM测试报告",
                           description="新增商机",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)




