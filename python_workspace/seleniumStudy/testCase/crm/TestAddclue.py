# -*- coding: utf-8 -*- 
# 2020/04/16 14:41 
# seleniumStudy
# TestAddclue.py
# company


import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from framework.BlueRose import BlueRose
from parameterized import parameterized
import datetime

from testCase.crm.BaseCase import BaseCase


class TestAddClue(BaseCase):

    #新增线索
    @parameterized.expand([
        ("测试客户1",'15112342277')
    ])
    def test_add_clue(self,contacts,mobile):
        # 点击客户管理
        self.driver.click("xpath=//span[text()='客户管理']")
        # 点击线索
        self.driver.click("id=leads-index")
        # 新建线索
        #self.driver.click("class=fa fa-plus-circle")
        self.driver.click('xpath=//i[@class="fa fa-plus-circle"]')
        # 输入联系人
        self.driver.send_keys('id=contacts_name',contacts)
        # 输入电话号码
        self.driver.send_keys('id=mobile',mobile)
        # 点击创建线索
        self.driver.click('id=save_submit')
        alert = self.driver.find_element('xpath=//*[@id="toast-container"]/div/div[2]')
        print(alert.text)
        assert alert.text == '线索添加成功！'



if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddClue)
    runer = HTMLTestRunner(title="简信CRM测试报告",
                           description="新增线索",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)




