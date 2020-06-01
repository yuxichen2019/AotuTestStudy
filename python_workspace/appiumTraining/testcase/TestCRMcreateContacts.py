# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower
from testcase.TestCRM import TestCRM


class TestCRMcreatebusiness(TestCRM):

    #  创建联系人
    def createContacts(self):

        # 点击联系人图标
        self.driver.click("text= 联系人 ")
        # 点击添加联系人按钮
        self.driver.click("text=sYVInwAAAABJRU5ErkJggg==")
        #选择所属客户
        self.driver.click("xpath=//*[@text='请选择']")
        self.driver.click("text=crm000001")
        self.driver.send_keys("xpath=//*[@text='请输入'][1]","yuanmei006")
        #选择角色
        # self.driver.click_index("id=vux-selector-ya9rv",0)
        # self.driver.click("text=角色*")
        # self.driver.click_index("class=android.widget.Spinner",0)
        self.driver.click("xpath=//android.widget.FrameLayout/android.widget.LinearLayout[@index=\"0\"]/android.widget.FrameLayout[@index=\"0\"]/android.widget.FrameLayout[@index=\"0\"]/com.tencent.tbs.core.webkit.WebView[@index=\"0\"]/android.webkit.WebView[@text=\"深圳公司\" and @index=\"0\"]/android.view.View[@index=\"0\"]/android.view.View[@index=\"0\"]/android.view.View[@index=\"0\"]/android.view.View[@index=\"0\"]/android.view.View[@index=\"1\"]/android.view.View[@index=\"0\"]/android.view.View[@index=\"4\"]/android.view.View[@index=\"1\"]/android.view.View[@index=\"1\"]/android.widget.Spinner[@index=\"0\"]")
        self.driver.click("text=普通人")
        #选择地址
        self.driver.click("text=地址*")
        self.driver.slideUP("xpath=//android.view.View[@text='北京市']")
        self.driver.click("xpath=//android.view.View[@text='完成']")

        #保存
        self.driver.click("xpath=//android.view.View[@text='保存']")
        #返回
        # self.driver.click_index("class=android.view.View",1)
        sleep(5)


    def test_weiChat(self):
        self.login()
        self.createContacts()
        # self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRM)
    runer = HTMLTestRunner(title="悟空CRM测试报告", description="登录", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
