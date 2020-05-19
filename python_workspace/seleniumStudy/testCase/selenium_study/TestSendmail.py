# -*- coding: utf-8 -*-
import os
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from selenium import webdriver
import unittest


class TestMail(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 谷歌浏览器
        self.driver = webdriver.Chrome()
        # 定义数组用来存放截图
        self.imgs = []
        # 最大化浏览器
        self.driver.maximize_window()
        self.driver.get("https://mail.163.com/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 增加截图
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_login(self):
        #账号密码登陆
        self.driver.find_element_by_id('lbNormal').click()
        login_frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]")
        #login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        #self.driver.switch_to.default_content()
        #输入账号
        self.driver.find_element_by_name('email').send_keys('15112342277')
        #输入密码
        self.driver.find_element_by_name('password').send_keys('yxc253676')
        #点击登陆
        self.driver.find_element_by_id('dologin').click()
        sleep(2)
        #点击写信
        self.driver.find_element_by_xpath('//span[text()="写 信"]').click()
        #输入收件人
        self.driver.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]').send_keys('15112342277')
        #输入主题
        self.driver.find_element_by_xpath('//input[contains(@id,"_subjectInput")]').send_keys('大家好')
        write_frame = self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']")
        self.driver.switch_to.frame(write_frame)
        #输入内容
        self.driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys('这是一封测试邮件')
        self.driver.switch_to.default_content()
        sleep(2)
        #点击发送
        self.driver.find_element_by_xpath('//span[@class="nui-btn-text" and text()="发送"]').click()
        sleep(2)

if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestMyPage_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    runer = HTMLTestRunner(title="我的界面测试报告", description="测试我的界面", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
