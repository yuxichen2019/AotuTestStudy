# -*- encoding:utf-8 -*-
import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class TestWeichat(unittest.TestCase):

    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': '*****',
            'platformVersion': '9',
            'automationName': 'UIAutomator2',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)  # 启动app

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        password = self.driver.find_element_by_id('com.tencent.mm:id/hx')
        password.clear()
        password.send_keys('**********')
        self.driver.find_element_by_id('com.tencent.mm:id/bwn').click()
        time.sleep(5)
        self.driver.find_element_by_class_name('android.widget.TextView').click()
        print('111111')
        time.sleep(5)
        find = self.driver.find_element_by_name('搜索')

        self.driver.find_element_by_xpath()
        find.send_keys('****')
        time.sleep(5)
        # 发文字
        self.driver.find_element_by_id('com.tencent.mm:id/l7').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.tencent.mm:id/aaa').send_keys('测试，请勿回复！')
        time.sleep(5)
        self.driver.find_element_by_id('com.tencent.mm:id/aag').click()
        time.sleep(5)
        # 发表情
        self.driver.find_element_by_id('com.tencent.mm:id/aac').click()
        self.driver.find_element_by_accessibility_id('[呲牙]').click()
        self.driver.find_element_by_id('com.tencent.mm:id/aag').click()
        time.sleep(5)
        # 发语音
        self.driver.find_element_by_id('com.tencent.mm:id/aa9').click()
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id('com.tencent.mm:id/aab')
        action1.long_press(el, None, None, 10000).perform()



if __name__ == '__main__':
    unittest.main()
