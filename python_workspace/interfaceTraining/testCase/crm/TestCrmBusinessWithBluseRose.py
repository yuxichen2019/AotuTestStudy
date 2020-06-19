import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from ddt import ddt, data, unpack

from framework.UtilsDate import UtilsDate
from framework.UtilsFile import UtilsFile
from framework.UtilsRandom import UtilsRandom
from testCase.student.BaseCase import BaseCase


@ddt
class TestCrmBusinessWithBluseRose(BaseCase):


    def createBusiness(self, phpsessid):
        # 随机生成中文名字
        chineseName = UtilsRandom.getChineseName()
        print("客户名称",chineseName)
        customerCode = UtilsDate.getCurrentDate("") + "_" + UtilsRandom.getNo(3)
        # 添加客户的URL
        url = self.baseURL + "m=business&a=add "
        # 请求数据
        # m = MultipartEncoder(
        #     fields = {'code': '20190414-0004',
        #         'owner_role_id': '1',
        #         'owner_name': 'gavin',
        #         'name': chineseName,
        #         'customer_id': '1434',
        #         'customer_name': '朱锄',
        #         'status_type_id': '1',
        #         'status_id': '1',
        #         'possibility': '10%',
        #         'submit': '保存商机'})
        data = {'code': '20190414-0004',
                  'owner_role_id': '1',
                  'owner_name': 'gavin',
                  'name': chineseName,
                  'customer_id': '1434',
                  'customer_name': '朱锄',
                  'status_type_id': '1',
                  'status_id': '1',
                  'possibility': '10%',
                  'submit': '保存商机'}
        # 请求头
        header = {'Content-Type':'application/x-www-form-urlencoded', 'Cookie': 'PHPSESSID=' + phpsessid}
        # 响应数据
        response = self.requests.sendRequests(url, data=data, headers=header)
        # 断言结果是否正确
        self.assertEqual(response.status_code, 200)

    @data(*UtilsFile.get_csv_data('userAccount.csv'))
    @unpack
    def test_crmBusinessFlow(self, username, password):
        print('current path is:', os.getcwd())
        """CRM创建客户"""
        # 刷新PHPSESSID
        loginInfo = self.refreshPhpSessId()
        # 登录
        self.login(loginInfo, username, password)
        # 创建客户
        self.createBusiness(loginInfo)


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCrmBusinessFlowWithBluseRose.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCrmBusinessWithBluseRose)
    runer = HTMLTestRunner(title="简信CRM", description="创建客户", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
