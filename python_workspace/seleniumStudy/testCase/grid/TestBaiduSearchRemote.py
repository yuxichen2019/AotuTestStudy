import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.BlueRose import BlueRose


class TestBaiduSearchRemote(unittest.TestCase):
    def setUp(self):
        # 火狐浏览器
        # self.driver = webdriver.Firefox()
        # 谷歌浏览器
        self.imgs = []
        self.driver = BlueRose(browser="chrome", isMultitask=True)
        # self.driver = BlueRose(browser="chrome")
        # 最大化浏器
        self.driver.max_window()

    def test_baiduSearchRemote(self):
        """百度测试来了"""
        # 打开百度
        self.driver.get("http://www.baidu.com")
        # 输入搜索内容
        self.driver.send_keys("id=kw", "selenium")
        # 点击查询按钮
        self.driver.click("id=su")
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBaiduSearchRemote)
    runner = HTMLTestRunner(title="百度搜索", description="这是一个百度搜索的自动化测试小例子", stream=open("Baidu_test_report.html", "wb"),
                            verbosity=2, retry=0, save_last_try=True)
    runner.run(suite)
