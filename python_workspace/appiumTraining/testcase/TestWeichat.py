# -*- encoding:utf-8 -*-
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from time import sleep
from testcase.BaseCase import BaseCase



class TestWebChat(BaseCase):
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
        count = 1
        while True:

            if count > 5:
                print('重复' + str(count) + '遍')
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
            self.driver.long_press("des=按住说话",10)

            # 点击 + 号
            self.driver.click('id=com.tencent.mm:id/ajp')
            #self.driver.click("text=更多功能按钮")
            # 点击拍摄
            self.driver.click_index("id=com.tencent.mm:id/p9",1)
            # 长按录制按钮3秒
            self.driver.long_press("id=com.tencent.mm:id/coe", 10)
            # 点击完成
            self.driver.click('id=com.tencent.mm:id/bfa')
            # 切换回键盘
            #self.driver.click("des=切换到键盘")
            sleep(1)
            count = count + 1

    def test_weiChat(self):
        self.searchFriend()
        self.sendMsgToFriend()

if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestMyPage_report.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebChat)
    runer = HTMLTestRunner(title="微信测试报告", description="测试微信发消息", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)


