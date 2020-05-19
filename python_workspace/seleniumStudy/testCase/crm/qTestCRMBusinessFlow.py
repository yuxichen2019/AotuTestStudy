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
class TestCRMBusinessFlow(BaseCase):
    # 创建客户
    def creatCustomer(self, customerName):
        # 打开客户管理
        self.driver.click("xpath=//span[contains(text(),'客户管理')]")
        # 点击客户管理列表下的客户
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=customer&a=index&by=me')]")

        # 点击新建客户
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=customer&a=add')]")
        # 输入姓名
        self.driver.send_keys("id=name", customerName)
        # 选择负责人
        self.driver.click("xpath=//input[@class='form-control required valid']")
        # 单击选择
        self.driver.click("xpath=//tr[@style='cursor:pointer']")
        # 点击确定
        self.driver.js("document.getElementsByClassName('ui-dialog-buttonset')[1].children[0].click()")

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

    # 创建商机
    def createBusinessOpportunity(self, customerName):
        self.driver.click("xpath=//span[contains(text(),'商机管理') and contains(@class,'nav-label')]")
        self.driver.click("id=business-index")
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=business&a=add')]")
        self.driver.send_keys("id=name", 'business' + UtilsDate.getCurrentTime())
        self.driver.click("id=customer_name")
        # 选择客户
        self.driver.click("xpath=//td[contains(text(),'" + customerName + "')]")
        self.driver.click("xpath=//span[contains(text(),'确认')]")
        self.driver.click("id=save_submit")

    # 创建合同
    def createContract(self, customerName):
        self.driver.click("xpath=//a[contains(@title,'合同订单')]")
        self.driver.click("id=contract-index")
        self.driver.click("xpath=//a[contains(@class,'btn btn-primary btn-sm pull-left')]")
        self.driver.send_keys("name=contract_name", 'contract' + UtilsDate.getCurrentTime())


        # 选择客户来源
        self.driver.click("id=customer_name")
        self.driver.click("xpath=//td[contains(text(),'" + customerName + "')]")
        self.driver.click("xpath=(//span[@class='ui-button-text' and text()='确定'])[3]")

        # 来源商机
        self.driver.click("id=business_name")
        self.driver.click("xpath=//td[contains(text(),'" + customerName + "')]")
        self.driver.click("xpath=(//span[@class='ui-button-text' and text()='确定'])[2]")
        # 合同金额
        self.driver.send_keys("id=contract_price", '100')
        # 签约时间
        self.driver.send_keys("id=due_time", UtilsDate.getCurrentDateAndTime())
        self.driver.js(
            "document.getElementById('add_body').children[0].children[0].children[0].children[0].scrollTop=10000;")
        # 合同到期时间
        self.driver.send_keys("id=end_date", UtilsDate.getCurrentDateAndTime())


        # 选择合同审批人
        self.driver.click("id=examine_role")
        self.driver.click("xpath=//td[contains(text(),'超级管理员')]")
        self.driver.click("xpath=//span[contains(text(),'确定')]")
        # self.driver.js(
        #     "document.getElementById('add_body').children[0].children[0].children[0].children[0].scrollTop=10000;")
        # 保存合同
        self.driver.click("id=save_submit")

    # @data(*UtilsFile.get_csv_data(filePath='account.csv'))
    # @unpack
    def test_crmBusinessFlow(self):
        """创建客户->创建商机->创建合同"""
        #self.login(username, password)
        customerName = UtilsRandom.getChineseName()
        print('new created customer name is:', customerName)
        self.creatCustomer(customerName)
        self.createBusinessOpportunity(customerName)
        self.createContract(customerName)


# if __name__ == "__main__":
#     report_path = os.path.dirname(__file__) + "/report/" + "TestCRMBusinessFlow.html"
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestCRMBusinessFlow)
#     runer = HTMLTestRunner(title="简信CRM测试报告",
#                            description="创建客户->创建商机->创建合同",
#                            stream=open(report_path, "wb"),
#                            verbosity=2, retry=0, save_last_try=True)
#     runer.run(suite)
