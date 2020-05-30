# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep

from testcase.BaseCase import BaseCase


class TestWebChat(BaseCase):

    # 登录微信
    def login(self):
        #切换验证方式
        #self.driver.click("id=com.tencent.mm:id/cqq")
        #用密码登录
        #self.driver.click("id=com.tencent.mm:id/l_")
        # 输入密码
        self.driver.send_keys("id=com.tencent.mm:id/bfl", "yb092226")
        # 点击登录
        self.driver.click("id=com.tencent.mm:id/d2y")

    # 退出微信登录
    def logout(self):
        # 点击返回
        self.driver.click("des=返回")
        # 点击返回
        self.driver.click("text=取消")
        # 点击我标签
        self.driver.click("text=我")
        # 点击设置
        self.driver.click("text=设置")
        # 向上滑动屏幕
        #self.driver.swipe_up(n=2)
        # 点击退出
        self.driver.click("text=退出")
        # 点击退出登录
        # self.driver.click("text=退出登录")
        # 点击退出
        self.driver.click("text=退出登录")
        self.driver.click("text=退出")



    # 查找好友
    def searchFriend(self):
        # 点击放大镜
        self.driver.click("id=com.tencent.mm:id/f4u")
        # 输入要搜索的好友名称
        self.driver.send_keys("id=com.tencent.mm:id/bfl", "yu")
        # 点击好友名称
        self.driver.click("id=com.tencent.mm:id/g8b")


    # 给好友发消息
    def sendMsgToFriend(self):
        count = 0
        while True:
            print('重复' + str(count) + '遍')

            if count > 1:
                break
            # 输入文字消息
            self.driver.send_keys("id=com.tencent.mm:id/ak7", "等你等了这么久"+str(count))
            # 点击发送按钮
            self.driver.click("id=com.tencent.mm:id/amr")
            # 点击表情按钮
            self.driver.click("des=表情")
            # 选择表情
            self.driver.click("des=[得意]")
            self.driver.click("des=[呲牙]")
            self.driver.click("des=[偷笑]")
            # 点击发送按钮
            self.driver.click("xpath=//android.widget.Button[@text=\"发送\"]")
            # 点击发送语音按钮
            self.driver.click("des=切换到按住说话")
            # 长按，按住说话
            self.driver.long_press("des=按住说话",1)

            # 点击 + 号
            self.driver.click('id=com.tencent.mm:id/ajp')
            #self.driver.click("text=更多功能按钮")
            # 点击拍摄
            self.driver.click_index("id=com.tencent.mm:id/p9",1)
            # 长按录制按钮3秒
            self.driver.long_press("id=com.tencent.mm:id/coe", 3)
            # 点击完成
            self.driver.click('id=com.tencent.mm:id/bfa')
            # 切换回键盘
            #self.driver.click("des=切换到键盘")
            sleep(2)
            count = count + 1
    def test_weiChat(self):
        # self.login()
        self.searchFriend()
        self.sendMsgToFriend()
        self.logout()


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestMyPage_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebChat)
    runer = HTMLTestRunner(title="微信测试报告", description="测试微信发消息", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
