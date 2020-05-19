# -*- coding: utf-8 -*- 
# 2020/4/19 11:37 
# seleniumStudy
# TestCrm.py 
# company

import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from framework.UtilsDate import UtilsDate
from framework.BlueRose import BlueRose
import datetime
from testCase.crm.BaseCase import BaseCase


class TestCrm(BaseCase):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = BlueRose(browser="chrome", isMultitask=False)
    #     self.driver.max_window()
    #     self.driver.get('https://my.jxycrm.com/index.php?m=user&a=login')
    #
    # # @classmethod
    # # def tearDownClass(self):
    # #     self.driver.quit()
    #
    # def setUp(self):
    #     self.login()
    #
    # def tearDown(self):
    #     pass
    #
    # def login(self):
    #     # 输入账号
    #     self.driver.send_keys("name=name", "15112342277")
    #     # 输入密码
    #     self.driver.send_keys('name=password', '123456')
    #     # 点击登录
    #     self.driver.click('id=loginsub')

    # #新增客户
    # def creat_customer(self):
    #     # 点击客户管理
    #     self.driver.click("xpath=//span[text()='客户管理']")
    #     # 点击客户
    #     self.driver.click("id=customer-index")
    #     # 新建客户
    #     # self.driver.click("class=btn btn-primary btn-sm pull-left") 不知道为什么用这一行为什么会报错
    #     self.driver.click('xpath=//a[@class="btn btn-primary btn-sm pull-left"]')
    #     # 输入客户名称
    #     self.driver.send_keys('id=name', '测试客户1')
    #     # 选择客户信息来源
         #self.driver.click('xpath=//option[contains(text(),"电话营销")]')
    #     # 点击创建客户
    #     self.driver.click('id=save_submit')
    #     alert = self.driver.find_element('xpath=//*[@id="toast-container"]/div/div[2]')
    #     if alert.text == '添加客户成功':
    #         print('客户添加成功')
    #     else:
    #         print('客户添加失败')
    #
    # #新增商机
    # def add_businessopportunity(self):
    #     #点击商机管理
    #     self.driver.click("xpath=//span[text()='商机管理']")
    #     #点击商机
    #     self.driver.click("id=business-index")
    #     #新建商机
    #     self.driver.click('xpath=//a[@class="btn btn-primary btn-sm pull-left"]')
    #     #点击选择客户
    #     self.driver.click('id=customer_name')
    #     #输入目标客户
    #     self.driver.send_keys('id=search',"测试客户1")
    #     #点击搜索
    #     self.driver.click("xpath=//button[text()='立即搜索']")
    #     sleep(1)
    #     #点击目标客户
    #     self.driver.click('xpath=//tbody[@id="datas"]/tr')
    #     #点击确定
    #     self.driver.click_index('xpath=//span[text()="确认"]',0)
    #     # 选择商机进度
    #     self.driver.click('xpath=//option[text()="完成收款"]')
    #     #时间-1-input的时间控件
    #     self.driver.send_keys("xpath=//input[@input_type='time']",'2020-04-28 16:28')
    #     #保存商机
    #     self.driver.click('id=save_submit')


    # 新增合同
    def test_creat_contract(self):
        #点击合同订单
        self.driver.click('xpath=//a[contains(@title,"合同订单")]')
        #点击合同
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=contract&a=index')]")
        #点击新建合同
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=contract&a=add')]")
        self.driver.send_keys('name=contract_name','测试合同1')
        self.driver.click("name=examine_role")
        self.driver.click('xpath=//td[contains(text(),"超级管理员")]')
        self.driver.click_index('xpath=//span[text()="确定"]',0)

        #选择来源客户
        self.driver.click("name=customer_name")
        self.driver.send_keys('id=search',"测试客户1")
        self.driver.click("xpath=//button[text()='立即搜索']")
        sleep(0.2)
        self.driver.click('xpath=//td[contains(text(),"测试客户1")]')
        self.driver.click("xpath=(//span[@class='ui-button-text' and text()='确定'])[3]")  #从1开始

        #选择商机
        self.driver.click('name=business_name')
        sleep(1)
        self.driver.click("xpath=(//td[contains(text(),'测试客户1')])[1]")
        sleep(1)
        self.driver.click('xpath=(//span[@class="ui-button-text" and text()="确定"])[2]')
        #输入合同金额
        self.driver.send_keys('id=contract_price','999999')
        #输入签约时间
        self.driver.send_keys('id=due_time',UtilsDate.getCurrentDate())
        #输入合同生效时间
        self.driver.send_keys('id=start_date',UtilsDate.getCurrentDate())

        #输入合同到期时间
        str1 = UtilsDate.getCurrentDate()

        list1=list(str1)
        list1[3]='1'
        str2 = ''.join(list1)
        self.driver.send_keys('id=end_date', str2)

        #点击保存合同
        self.driver.click('id=save_submit')
        #self.driver.click('xpath=//button[contains(text(),"保存合同")]')


if __name__ == "__main__":
    #report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    #在当前文件目录设置 'report/文件名' 的文件夹
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, "%Y_%m_%d_%H_%M_%S")
    REPORT_DIR = os.path.split(__file__)[0] + '/report/' + os.path.splitext(os.path.split(__file__)[1])[0] + time_str
    if os.path.exists(REPORT_DIR):
        pass
    else:
        os.makedirs(REPORT_DIR)

    #report_path = os.path.join(REPORT_DIR, time_str, "TestCRMAddcustomer.html")
    report_path = REPORT_DIR  + "/TestCRMAddcustomer.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCrm)
    runer = HTMLTestRunner(title="我的界面测试报告", description="测试我的界面", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)