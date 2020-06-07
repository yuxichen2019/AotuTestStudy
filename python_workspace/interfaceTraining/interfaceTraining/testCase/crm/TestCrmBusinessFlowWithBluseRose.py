import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from ddt import ddt, data, unpack

from framework.UtilsDate import UtilsDate
from framework.UtilsRandom import UtilsRandom
from testCase.student.BaseCase import BaseCase


@ddt
class TestCrmBusinessFlowWithBluseRose(BaseCase):

    # 创建客户
    def createCustomer(self, phpsessid):
        # 随机生成中文名字
        chineseName = UtilsRandom.getChineseName()
        print("客户名称",chineseName)
        customerCode = UtilsDate.getCurrentDate("") + "_" + UtilsRandom.getNo(3)
        # 添加客户的URL
        url = self.baseURL + "m=customer&a=add"
        # 请求数据
        data = {"name": chineseName,
                "owner_role_id": "1",
                "owner_name": "gavin",
                "nextstep_time": "",
                "customer_code": customerCode,
                "customer_status": "意向客户",
                "industry": "",
                "address[city]": "市辖区",
                "address[area]": "",
                "address[street]": "",
                "origin": "电话营销",
                "grade": "",
                "no_of_employees": "",
                "description": "",
                "con_contacts[name]": "",
                "con_contacts[role]": "",
                "con_contacts[post]": "",
                "con_contacts[telephone]": "",
                "con_contacts[qq_no]": "",
                "con_contacts[email]": "",
                "con_contacts[contacts_address][state]": "北京市",
                "con_contacts[contacts_address][city]": "市辖区",
                "con_contacts[contacts_address][area]": "",
                "con_contacts[contacts_address][street]": "",
                "con_contacts[zip_code]": "",
                "con_contacts[description]": ""}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "Cookie": "PHPSESSID=" + phpsessid}
        # 响应数据
        response = self.requests.sendRequests(url, data=data, headers=header)
        # 断言结果是否正确
        self.assertEqual(response.status_code, 200)
    #  创建商机
    def createBusinessOpportunity(self,phpsessid):
        busniessCode = UtilsDate.getCurrentDate("") + "-" + UtilsRandom.getNo(4)
        # 新增商机的URL
        businessName = UtilsRandom.getChineseName()
        url = self.baseURL + "m=business&a=add"
        # 请求数据
        data = {"code":busniessCode,
                "owner_role_id":"1",
                "owner_name": "超级管理员",
                "name":businessName,
                "customer_id":"32",
                "customer_name":"严三新",
                "contacts_id":"16",
                "contacts_name":"金襟分",
                "status_type_id":"1",
                "status_id":"1",
                "possibility":"10%",
                "submit":"保存商机"}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "Cookie": "PHPSESSID=" + phpsessid}
        # 响应数据
        response = self.requests.sendRequests(url, data=data, headers=header)
        # 断言结果是否正确
        self.assertEqual(response.status_code, 200)

    # @data(*UtilsFile.get_csv_data(filePath='../../data/userAccount.csv'))
    @data(['19926451606','900e0313b981caa9f83ed5d0a01e9c58'])
    @unpack
    def test_crmBusinessFlow(self, username, password):
        """CRM创建客户"""
        # 刷新PHPSESSID
        loginInfo = self.refreshPhpSessId()
        # 登录
        self.login(loginInfo, username, password)
        # 创建客户
        self.createCustomer(loginInfo)
        # 创建商机
        self.createBusinessOpportunity(loginInfo)


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCrmBusinessFlowWithBluseRose.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCrmBusinessFlowWithBluseRose)
    runer = HTMLTestRunner(title="简信CRM", description="创建客户", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
