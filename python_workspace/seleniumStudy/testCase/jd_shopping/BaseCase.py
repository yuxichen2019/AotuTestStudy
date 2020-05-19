import unittest
from time import sleep
from framework.BlueRose import BlueRose
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException



class BaseCase(unittest.TestCase):

    def setUp(self):
        # 谷歌浏览器
        self.driver = BlueRose(browser="chrome", isMultitask=False)
        # 最大化浏览器
        self.driver.max_window()
        # 打开网页
        #self.driver.get("https://www.jd.com/")
        self.driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_526784f38767411da7e53da828652edc")


    # def tearDown(self):
    #     self.driver.quit()

    def login(self, user, passwd):
        self.driver.click('xpath=//a[@class="link-login"]')
        self.driver.click('xpath=//a[contains(text(),"账户登录")]')
        self.driver.send_keys("id=loginname", user)
        self.driver.send_keys("id=nloginpwd", passwd)
        self.driver.click("id=loginsubmit")

        # slider=self.driver.find_element("xpath=//div[@class='JDJRV-slide-inner JDJRV-slide-btn']")
        #
        # action = ActionChains(self.driver)
        # action.click_and_hold(slider).perform()
        #
        # for i in range(200):
        #
        #     try:
        #         action.move_by_offset(2,0).perform()
        #     except UnexpectedAlertPresentException:
        #         break
        #     action.reset_actions()
        #     sleep(0.2)
        #
        # success_text = self.driver.switch_to.alert.text
        # print(success_text)