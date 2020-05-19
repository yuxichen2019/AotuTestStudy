# -*- coding: utf-8 -*- 
# 2020/4/19 15:17 
# seleniumStudy
# Upload.py 
# company
#此文件包括sendkeys 和 Autoit 两种方式的上传文件


import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from framework.BlueRose import BlueRose
import datetime

class UploadCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=BlueRose(browser="chrome",isMultitask=False)
        self.driver.max_window()
        self.driver.get('https://my.jxycrm.com/index.php?m=user&a=login')

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

    def setUp(self):
        self.login()

    def tearDown(self):
        pass

    def login(self):
        #输入账号
        self.driver.send_keys("name=name", "15112342277")
        #输入密码
        self.driver.send_keys('name=password','123456')
        #点击登录
        self.driver.click('id=loginsub')


    # 上传客户
    def test_upload(self):
        #点击客户管理
        self.driver.click("xpath=//span[text()='客户管理']")
        #点击客户
        self.driver.click("id=customer-index")
        #点击操作
        self.driver.click('xpath=//button[text()="操作 "]')
        #点击导入
        self.driver.click('id=import_excel')
        sleep(1)
        #点击选择文件
        #self.driver.click("xpath=//p[@id='attachment1']/input")
        self.driver.js(
            "document.getElementById('file').click()")
        sleep(1)
        #上传文件
        os.system(r'E:\study\python_workspace\seleniumStudy\Autoit\au3.exe')
        # 点击确定
        self.driver.click("xpath=(//span[text()='确定' and @class='ui-button-text'])[4]")




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
    suite = unittest.TestLoader().loadTestsFromTestCase(UploadCustomer)
    runer = HTMLTestRunner(title="我的界面测试报告", description="测试我的界面", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)




