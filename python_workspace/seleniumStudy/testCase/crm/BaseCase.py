import unittest
from framework.BlueRose import BlueRose


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 谷歌浏览器
        self.driver = BlueRose(browser="chrome", isMultitask=False)
        # 最大化浏览器
        self.driver.max_window()
        # 打开网页
        self.driver.get("http://my.crm.cc/index.php?m=user&a=login")
        #self.login('15112342277','yxc253676')
        self.driver.send_keys("id=name", '15112342277')
        self.driver.send_keys("id=password", '123456')
        self.driver.click("id=loginsub")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

