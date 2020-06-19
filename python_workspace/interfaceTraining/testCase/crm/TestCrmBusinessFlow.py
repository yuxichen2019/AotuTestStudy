import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

import requests
import json

from framework.UtilsDate import UtilsDate
from framework.UtilsRandom import UtilsRandom


class TestCreateCustomer(unittest.TestCase):
    def setUp(self):
        self.baseURL = "http://my.jxycrm.com/"

    def tearDown(self):
        pass

    def refreshPhpSessId(self):
        # 登录url地址
        url = self.baseURL + "index.php?m=user&a=login"
        # 响应报文
        response = requests.get(url, verify=False)
        # 获取cookie的值
        phpsessid = requests.utils.dict_from_cookiejar(response.cookies)['PHPSESSID']
        # 字典
        dict = {'PHPSESSID': phpsessid}
        print("登录获取的PHPSESSID:" + dict['PHPSESSID'])
        return dict

    def login(self, phpsessid):
        # 登录url地址
        url = self.baseURL + "index.php?m=user&a=login"
        # 请求参数
        data = {"name": "19926451606", "password": "900e0313b981caa9f83ed5d0a01e9c58", "config_id": ""}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "utf-8",
                  "Cookie": "PHPSESSID=" + phpsessid}
        # 响应报文
        response = requests.post(url, data=data, headers=header, verify=False)
        info = json.loads(response.content)['info']
        self.assertEqual(info, "登录成功")

    def createCustomer(self, phpsessid):
        # 随机生成中文名字
        chineseName = UtilsRandom.getChineseName()
        customerCode = UtilsDate.getCurrentDate("") + "_" + UtilsRandom.getNo(3)
        print("创建的客户是：", chineseName)
        # 添加客户的URL
        url = self.baseURL + "index.php?m=customer&a=add"
        # 请求数据
        # data = {"refer_url": "https://my.crm.cc/index.php?m=customer&a=index&by=me",
        #         "name": chineseName,
        #         "owner_role_id": "1",
        #         "owner_name": "gavin",
        #         "nextstep_time": "",
        #         "customer_code": customerCode,
        #         "customer_status": "意向客户",
        #         "industry": "",
        #         "address[city]": "市辖区",
        #         "address[area]": "",
        #         "address[street]": "",
        #         "origin": "电话营销",
        #         "grade": "",
        #         "no_of_employees": "",
        #         "description": "",
        #         "con_contacts[name]": "",
        #         "con_contacts[role]": "",
        #         "con_contacts[post]": "",
        #         "con_contacts[telephone]": "",
        #         "con_contacts[qq_no]": "",
        #         "con_contacts[email]": "",
        #         "con_contacts[contacts_address][state]": "北京市",
        #         "con_contacts[contacts_address][city]": "市辖区",
        #         "con_contacts[contacts_address][area]": "",
        #         "con_contacts[contacts_address][street]": "",
        #         "con_contacts[zip_code]": "",
        #         "con_contacts[description]": ""}
        data = {"refer_url": "https://my.crm.cc/index.php?m=customer&a=index&by=me",
                "name": chineseName,
                "owner_role_id": "1",
                "owner_name": "gavin",
                "customer_code": chineseName,
                "customer_status": "意向客户",
                "address[city]": "市辖区",
                "origin": "电话营销",
                "con_contacts[contacts_address][state]": "北京市",
                "con_contacts[contacts_address][city]": "市辖区"}
        # 请求头
        header = {"Content-Type": "application/x-www-form-urlencoded", "Cookie": "PHPSESSID=" + phpsessid}
        # 响应数据
        response = requests.post(url, data=data, headers=header, verify=False)
        # 响应结果转化为json
        # print("返回结果",response.content)
        # info = json.loads(response.content)['info']
        # # 断言结果是否正确
        # self.assertEqual(info, "添加成功！")

    def test_crmBusinessFlow(self):
        """CRM创建客户"""
        loginInfo = self.refreshPhpSessId()
        self.login(loginInfo['PHPSESSID'])
        self.createCustomer(loginInfo['PHPSESSID'])


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestCRM.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateCustomer)
    runner = HTMLTestRunner(title="简信CRM", description="自动化测试", stream=open(report_path, "wb"),
                            verbosity=2, retry=0, save_last_try=True)
    runner.run(suite)
