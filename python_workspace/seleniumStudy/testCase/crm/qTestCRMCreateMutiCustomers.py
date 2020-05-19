import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from ddt import data, unpack, ddt

from framework.UtilsDate import UtilsDate
from framework.UtilsFile import UtilsFile
from framework.UtilsRandom import UtilsRandom
from testCase.crm.BaseCase import BaseCase


@ddt
class TestCRMCreateMutiCustomers(BaseCase):
    # 创建客户
    def creatCustomer(self, customerName):
        # 点击新建客户
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=customer&a=add')]")
        # 输入姓名
        self.driver.send_keys("id=name", customerName)
        print('当前时间',UtilsDate.getCurrentDateAndTime())
        self.driver.send_keys("id=nextstep_time", UtilsDate.getCurrentDateAndTime())
        self.driver.js(
            "document.getElementById('add_body').children[0].children[0].children[0].children[0].scrollTop=10000;")
        # 选择下拉列表方式1
        self.driver.click("xpath=//option[contains(@value,'电话营销')]")
        # 首要联系人名称
        self.driver.send_keys("id=con_contacts[name]", customerName)
        # 选择角色
        self.driver.find_element("id=con_contacts[role]").send_keys("普通人")
        # 选择尊称,报错
        self.driver.click("xpath=//label[contains(text(),'女士')]")
        # 输入手机号
        self.driver.send_keys("id=con_contacts[telephone]", UtilsRandom.getMobilePhone())
        # 输入邮箱
        self.driver.send_keys("id=con_contacts[email]", "820061154@qq.com")
        self.driver.click("id=save_submit")
        success = self.driver.find_element("xpath=//span[contains(text(),'" + customerName + "')]")
        self.assertTrue(success.is_displayed())

    # @data(*UtilsFile.get_csv_data(filePath='account.csv'))
    # # @data(['19926451606','ujm159yhn753'],['13126321822','admin1234'])
    # @unpack
    # def test_crmBusinessFlow(self, username, password):
    #     """多个账号循环创建多个客户"""
    #     self.login(username, password)
    #     # 打开客户管理
    #     self.driver.click("xpath=//span[contains(text(),'客户管理')]")
    #     # 点击客户管理列表下的客户
    #     self.driver.click("xpath=//a[contains(@href,'/index.php?m=customer&a=index&by=me')]")
    #     for num in range(5):
    #         customerName = UtilsRandom.getChineseName()
    #         print('new created customer name is:', customerName)
    #         self.creatCustomer(customerName)
    #         sleep(3)

if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRMCreateMutiCustomers)
    runer = HTMLTestRunner(title="简信CRM测试报告",
                           description="创建客户->创建商机->创建合同",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)

