import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from framework.BlueRose import BlueRose


class TestMail163(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 谷歌浏览器
        self.driver = BlueRose(browser="chrome", isMultitask=False)
        # 最大化浏览器
        self.driver.max_window()
        # 打开163邮箱网页
        self.driver.get("https://mail.163.com/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 登录
    def login(self):
        # 点击密码登录
        self.driver.click("id=lbNormal")
        # 切换iframe
        self.driver.switch_to_frame("xpath=//iframe[starts-with(@id,'x-URS-iframe')]")
        # 输入账号
        self.driver.send_keys("name=email", "15112342277")
        # 输入密码
        self.driver.send_keys("name=password", "yxc253676")
        # 点击【登陆】
        self.driver.click("id=dologin")

    # 写信
    def test_sendEmail(self):

        self.login()
        sleep(1)
        # 点击写信
        self.driver.click("xpath=//span[contains(text(), '写 信')]")
        # 输入收信人
        self.driver.send_keys("class=nui-editableAddr-ipt", "seleniumtraining@163.com")
        # 输入主题
        self.driver.send_keys(
            "xpath=//input[contains(@class,'nui-ipt-input') and contains(@maxlength,'256') and contains(@type,'text')]",
            "163测试邮件主题")
        # 切换到iframe
        self.driver.switch_to_frame("class=APP-editor-iframe")
        # 输入内容“内容”
        self.driver.send_keys("class=nui-scroll","163测试邮件内容")
        # 退出ifream
        self.driver.switch_to_default()
        # 点击【发送】
        self.driver.click("class=nui-toolbar-item")
        success = self.driver.find_element("xpath=//h1[contains(text(), '发送成功')]")
        self.assertTrue(success.is_displayed())


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestMail163_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail163)
    runer = HTMLTestRunner(title="网易邮箱测试报告",
                           description="163发送邮件测试百度搜索",
                           stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
