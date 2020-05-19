# -*- coding: utf-8 -*- 
# 2020/04/16 11:39 
# seleniumStudy
# TestAddcustomer.py
# company


import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from ddt import unpack, data, ddt

from framework.UtilsFile import UtilsFile
from framework.UtilsRandom import UtilsRandom
from selenium.webdriver.support.select import Select
import datetime

from testCase.crm.BaseCase import BaseCase

@ddt
class TestAddCustomer(BaseCase):
    @data(*UtilsFile.get_csv_data(filePath='account.csv'))
    #@data(['15112342277','123456'],
    #      ['19926451606','ujm159yhn753'],
    #      ['13126321822','admin1234'])
    @unpack
    def test_add_customer(self,username,password):

        self.login(username,password)
        # 点击客户管理
        self.driver.click("xpath=//span[text()='客户管理']")
        # 点击客户
        self.driver.click("id=customer-index")

        for i in range(5):
            customer=UtilsRandom.getChineseName()
            #新建客户
            #self.driver.click("class=btn btn-primary btn-sm pull-left") 不知道为什么用这一行为什么会报错
            self.driver.click('xpath=//a[@class="btn btn-primary btn-sm pull-left"]')
            #输入客户名称
            self.driver.send_keys('id=name',customer)
            #选择客户信息来源
            Select(self.driver.find_element('id=origin')).select_by_value('电话营销')
            #点击创建客户
            self.driver.click('id=save_submit')
            success = self.driver.find_element("xpath=//span[contains(text(),'" + customer + "')]")
            self.assertTrue(success.is_displayed())



if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddCustomer)
    runer = HTMLTestRunner(title="简信CRM测试报告",
                           description="创建客户",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)



