import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from ddt import ddt, data, unpack

from framework.UtilsDate import UtilsDate
from framework.UtilsFile import UtilsFile
from framework.UtilsRandom import UtilsRandom
from testCase.BaseCase import BaseCase


@ddt
class TestProductWithBluseRose(BaseCase):

    # 创建产品
    def createProduct(self, phpsessid):
        # 随机生成中文名字
        productName = UtilsRandom.getChineseName()
        print("产品名称",productName)
        url = self.baseURL + "m=product&a=add"
        # 请求数据
        data = {"name":productName,
                "category_id":"1",
                "standard":"个",
                "has_sn":"0",
                "enable_spec":"0"}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "Cookie": "PHPSESSID=" + phpsessid}
        # 响应数据
        response = self.requests.sendRequests(url, data=data,method="post", headers=header)
        # 断言结果是否正确
        self.assertEqual(response.status_code, 200)
    #  创建商机

    @data(*UtilsFile.get_csv_data(filePath='userAccount.csv'))
    # @data(['19926451606','900e0313b981caa9f83ed5d0a01e9c58'])
    @unpack
    def test_createProduct(self, username, password):
        """CRM创建客户"""
        # 刷新PHPSESSID
        loginInfo = self.refreshPhpSessId()
        # 登录
        self.login(loginInfo, username, password)
        # 创建产品
        for next in range(0, 5):
            self.createProduct(loginInfo)


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCrmBusinessFlowWithBluseRose.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProductWithBluseRose)
    runer = HTMLTestRunner(title="简信CRM", description="创建客户", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
