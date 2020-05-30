# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from framework.SunFlower import SunFlower


class TestWebChat(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 模拟器
        # self.driver = SunFlower("192.168.136.101:5555", "5.1", "com.tencent.mm", "com.tencent.mm.ui.LauncherUI")
        # 三星手机
        self.driver = SunFlower("7eaeef32", "9", "com.tencent.mm",
                                "com.tencent.mm.ui.LauncherUI")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 登录微信
    def login(self):
        #切换验证方式
        self.driver.click("id=com.tencent.mm:id/cqq")
        #用密码登录
        self.driver.click("id=com.tencent.mm:id/l_")
        # 输入密码
        self.driver.send_keys("id=com.tencent.mm:id/l3", "password123")
        # 点击登录
        self.driver.click("id=com.tencent.mm:id/cqc")

    # 退出微信登录
    def logout(self):
        # 点击返回
        self.driver.click("des=返回")
        # 点击返回
        self.driver.click("des=返回")
        # 点击我标签
        self.driver.click("text=我")
        # 点击设置
        self.driver.click("text=设置")
        # 向上滑动屏幕
        self.driver.swipe_up(n=2)
        # 点击退出
        self.driver.click("text=退出")
        # 点击退出登录
        # self.driver.click("text=退出登录")
        # 点击退出
        self.driver.click("text=退出登录")
        self.driver.click("text=退出")



    # 查找好友
    def searchFriend(self):
        # 点击通讯录
        self.driver.click("text=通讯录")
        # 点击查询
        self.driver.click("id=com.tencent.mm:id/jb")
        # 输入要搜索的好友名称

        self.driver.send_keys("id=com.tencent.mm:id/l3", "Ymei")

        # 点击好友名称
        self.driver.click("id=com.tencent.mm:id/qm")


    # 给好友发消息
    def sendMsgToFriend(self):
        count = 0
        while True:
            print('重复' + str(count) + '遍')
            count = count + 1
            if count == 2:
                break
            # 输入文字消息
            self.driver.send_keys("id=com.tencent.mm:id/ami", "等你等了这么久")
            # 点击发送按钮
            self.driver.click("id=com.tencent.mm:id/amp")
            # 点击表情按钮
            self.driver.click("id=com.tencent.mm:id/amk")
            # 选择表情
            self.driver.click("des=[闭嘴]")
            self.driver.click("des=[撇嘴]")
            self.driver.click("des=[色]")
            # 点击发送按钮
            self.driver.click("xpath=//android.widget.Button[@text=\"发送\"]")

            # 点击发送语音按钮
            self.driver.click("des=切换到按住说话")
            # # 长按，按住说话
            # self.driver.long_press("xpath=//android.widget.Button[@text=\"按住 说话\"]", 10)
            self.driver.long_press("des=按住说话", 10)

            # # 切换回键盘
            self.driver.click("des=切换到键盘")

    def test_weiChat(self):
        self.login()
        self.searchFriend()
        self.sendMsgToFriend()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestMyPage_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebChat)
    runer = HTMLTestRunner(title="微信测试报告", description="测试微信发消息", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
