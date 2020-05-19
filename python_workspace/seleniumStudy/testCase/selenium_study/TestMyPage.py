# -*- coding: utf-8 -*-
import os
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from selenium import webdriver
import unittest


class TestMyPage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 谷歌浏览器
        self.driver = webdriver.Chrome()
        # 定义数组用来存放截图
        self.imgs = []
        # 最大化浏览器
        self.driver.maximize_window()
        self.driver.get("file:///E:/study/python_workspace/seleniumStudy/pages/seleniumTraining.html")
        print("第一个执行我这里")
    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
    #     print("最后执行我这里")
    # 增加截图
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
    def test_myPage(self):
        print("第二个执行我这里")
        inputList = self.driver.find_elements_by_tag_name("input")
        print(inputList)
        self.add_img()
        # 文本框输入值
        inputList[0].send_keys("这是个文本框")
        # 点击checkbox
        inputList[1].click()
        # 输入密码
        inputList[2].send_keys("123456789")
        # 点击单选框
        inputList[3].click()
        # 循环遍历select选择框
        allOptions = self.driver.find_elements_by_tag_name("option")
        for option in allOptions:
            print("Value is: " + option.get_attribute("value"))
            option.click()
            self.add_img()
            sleep(1)
        self.driver.find_element_by_id("clickme").click()
        sleep(3)
        # self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.dismiss()
        sleep(10)
        self.driver.switch_to.alert.accept()


if __name__ == "__main__":
    report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    if os.path.exists(report_path):
        pass
    else:
        os.makedirs(report_path)
    report_path = report_path + "\TTestMyPage_report.html"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyPage)
    runer = HTMLTestRunner(title="我的界面测试报告", description="测试我的界面", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)

