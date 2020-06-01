import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from asyncio import sleep

from framework.SunFlower import SunFlower


class TestWeibo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 华为手机
        self.driver = SunFlower("192.168.136.101:5555", "5.1", "com.sina.weibo", "com.sina.weibo.SplashActivity")
        # self.driver.switch_to_webViewOrNative()
        sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 登录账号
    def login(self):
        # 账号密码登陆
        self.driver.touch_tap(36, 89)
        self.driver.click("id=com.sina.weibo:id/tv_login_more_questions")
        self.driver.send_keys("text=请输入登录密码", "chenyiwei")
        self.driver.click("text=登录")

    # 给用户发消息
    def follow(self):
        # 进入消息页面
        self.driver.send_keyEvent(66)
        self.driver.click(
            "xpath=//android.widget.FrameLayout/android.widget.LinearLayout[@index=\"0\"]/android.widget.FrameLayout[@index=\"0\"]/android.widget.TabHost[@index=\"0\"]/android.widget.LinearLayout[@index=\"3\"]/android.view.View[@index=\"0\"]")
        self.driver.click("des=登录")
        self.driver.click("id=com.sina.weibo:id/tv_search_keyword")
        self.driver.send_keys("id=com.sina.weibo:id/tv_search_keyword", "卖鱼弟")
        # self.driver.touch_tap(216, 1788)
        # 进入新浪新闻
        self.driver.click("text=新浪新闻")
        # 搜索“卖鱼弟”
        self.driver.click("id=com.sina.weibo:id/et_message")
        self.driver.send_keys("id=com.sina.weibo:id/et_message", "卖鱼弟")
        self.driver.click("text=发送")

    # 退出微博
    def quit(self):
        # 返回主页面
        self.driver.click("id=com.sina.weibo:id/back")
        # 进入我的-设置页面
        self.driver.click("class=android.view.ViewGroup")
        self.driver.click("text=设置")
        # 退出微博
        self.driver.swipe_up()
        self.driver.click("text=退出微博")
        self.driver.click("text=确定")

    def test_weibo(self):
        # self.login()
        self.follow()
        # self.quit()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestWeibo_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeibo)
    runer = HTMLTestRunner(title="微博测试报告", description="测试关注", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
