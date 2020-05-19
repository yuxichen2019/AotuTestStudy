import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from ddt import ddt, data, unpack

from framework.BlueRose import BlueRose


@ddt
class TestBaiduSearchWithParameter(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 谷歌浏览器
        self.driver = BlueRose(browser="chrome", isMultitask=False)
        # 最大化浏览器
        self.driver.max_window()
        #self.driver.get("http://www.baidu.com")
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def setUp(self):
        self.driver.get("http://www.baidu.com")

    @data(['java', 'Java'],
          ['github', 'github'],
          ['python', 'python'])
    @unpack
    def test_baiduSearch(self, input, expect):
        """百度数据驱动测试"""
        self.driver.send_keys("id=kw", input)  # 该元素位置输入内容
        self.driver.click("id=su")
        print("这里是第一列的数据"+input)
        print("这里是第二列的数据"+expect)
        sleep(3)
        expectResult = self.driver.find_element("xpath=//em[contains(text(), '" + expect + "')]")
        self.assertTrue(expectResult.is_displayed())


if __name__ == "__main__":
    # 创建报告的路径
    report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    if os.path.exists(report_path):
        pass
    else:
        # 创建多层级的文件夹
        os.makedirs(report_path)
    report_path = report_path + "\TestBaiduSearchWithParameter_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBaiduSearchWithParameter)
    runer = HTMLTestRunner(title="带截图的测试报告", description="小试牛刀", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
