# -*- coding: utf-8 -*- 
# 2020/04/16 14:46 
# seleniumStudy
# TestDeletecustomer.py 
# company


import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from parameterized import parameterized
from testCase.crm.BaseCase import BaseCase


class TestDeleteCustomer(BaseCase):

    # 删除客户
    @parameterized.expand([
        ("测试客户1")
        ])
    def test_delete_customer(self,customername):
        #点击客户管理
        self.driver.click("xpath=//span[text()='客户管理']")
        #点击客户
        self.driver.click("id=customer-index")
        #搜索栏输入客户
        self.driver.send_keys('id=short_search',customername)
        #点击搜索
        self.driver.click('id=short_search_btn')
        #勾选搜索结果()
        self.driver.click('xpath=//*[@id="tab_Test3"]/tbody/tr[2]/td[1]/div')
        #点击删除
        self.driver.click('id=delete')
        #确定删除
        self.driver.click("xpath=//button[@tabindex='1']")
        self.wait(1)
        # 点击客户
        self.driver.click("id=customer-index")
        #搜索栏输入客户
        self.driver.send_keys('id=short_search',customername)
        #点击搜索
        self.driver.click('id=short_search_btn')
        #搜索结果数量
        result = self.driver.get_text("xpath=//*[@id='tfoot_page']/span/span")
        assert result == '0'


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteCustomer)
    runer = HTMLTestRunner(title="简信CRM测试报告",
                           description="创建客户->创建商机->创建合同",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)

