import os
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

from framework.Logger import Logger


class SunFlower(object):
    def __init__(self, deviceName, platformVersion, appPackage, appActivity):
        """
            构造方法实例化appium driver
            :param deviceName: 设备名
            :param platformVersion: 版本号
            :param appPackage: app package
            :param appActivity: 启动 activity
        """
        self.logger = Logger('sunFlower.log', level='debug').logger
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': deviceName,
            'platformVersion': platformVersion,
            'automationName': 'UIAutomator2',
            'appPackage': appPackage,
            'appActivity': appActivity,
            # 这两个属性设置支持中文输入
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            # True不会清除缓存数据
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(5)

    def wait_element(self, element, seconds=30):
        """
        智能等待android元素
        :param element: android元素的定位方式
        :param seconds: 等待的超时时间，默认30秒
        :return: 无
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")
        try:
            by = element[0:element.find("=")]
            value = element[element.find("=") + 1:len(element)]
            if by == "id":
                WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_id(value))
            elif by == "text":
                WebDriverWait(self.driver, seconds).until(
                    lambda x: x.find_element_by_android_uiautomator("new UiSelector().text(\"" + value + "\")"))
            elif by == "class":
                WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_class_name(value))
            elif by == "xpath":
                WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_xpath(value))
            elif by == "des":
                WebDriverWait(self.driver, seconds).until(lambda x: x.find_element_by_accessibility_id(value))
            else:
                self.logger.error(
                    "Please enter the correct targeting elements,'id','class','text','xpath','content-des'.")
                raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")
        except Exception:
            self.logger.exception("Time out can not find the element,the screen shot is:" + self.get_screenshot())
            assert False

    def find_element(self, element):
        """
        查找android元素
        :param element: android元素的定位方式
        :return: 无
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element[0: element.find("=")]
        value = element[element.find("=") + 1: len(element)]

        if by == "id":
            return self.driver.find_element_by_id(value)
        # android 的text属性可以通过name方法来定位
        elif by == "text":
            return self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + value + "\")")
        # 通过class属性定位元素需要与索引一同使用
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        # Android定位是有xpath属性的
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        # des就是android的content-des
        elif by == "des":
            return self.driver.find_element_by_accessibility_id(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','class','text','xpath','content-des'.")

    def find_elements(self, element, index):
        """
        查找android元素
        :param element:android元素的定位方式
        :param index: 元素下标
        :return:
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element[0: element.find("=")]
        value = element[element.find("=") + 1: len(element)]

        if by == "id":
            return self.driver.find_elements_by_id(value)[index]
        # android 的text属性可以通过name方法来定位
        elif by == "text":
            return self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"" + value + "\")")[index]
        # 通过class属性定位元素需要与索引一同使用
        elif by == "class":
            return self.driver.find_elements_by_class_name(value)[index]
        # Android定位是有xpath属性的
        elif by == "xpath":
            return self.driver.find_elements_by_xpath(value)[index]
        # des就是android的content-des
        elif by == "des":
            return self.driver.find_elements_by_accessibility_id(value)[index]
        else:
            raise NameError("Please enter the correct targeting elements,'id','class','text','xpath','content-des'.")

    def click_index(self, element, index):
        """
        通过索引点击android元素
        :param element: android元素的定位方式
        :param index: 元素数组下标
        :return:
        """
        self.wait_element(element)
        self.find_elements(element, index).click()

    def click(self, element):
        """
        点击android元素
        :param element: 定位android元素的方式
        :return: 无
        """
        self.wait_element(element)
        self.find_element(element).click()

    def send_keys(self, element, text):
        """
        android元素的输入操作
        :param element: android元素的定位方式
        :param text: android元素的输入内容
        :return: 无
        """
        self.wait_element(element)
        androidElement = self.find_element(element)
        androidElement.clear()
        androidElement.send_keys(text)

    def send_keys_index(self, element, index, text):
        """
        android元素输入操作
        :param element: android元素的定位方式
        :param index: 元素的数组下标
        :param text: 输入的文本内容
        :return:
        """
        self.wait_element(element)
        androidElement = self.find_elements(element, index)
        androidElement.clear()
        androidElement.send_keys(text)

    def long_press(self, element, times):
        """
        长按android元素
        :param element: android元素的定位方式
        :param times: 长按的时间
        :return: 无
        """
        self.wait_element(element)
        androidElement = self.find_element(element)
        touchAction = TouchAction(self.driver)
        touchAction.long_press(androidElement, None, None, times * 1000).perform()

    def send_keyEvent(self,keyCode):
        """
        模拟发送键盘事件
        :param keyCode: KEYCODE_ENTER 回车键 66
        :return:
        """
        self.driver.keyevent(keyCode)

    def swipe_up(self, t=500, n=1):
        """
        向上滑动屏幕
        :param t: 持续时长
        :param n: 滑动的步长
        :return:
        """
        window_size = self.driver.get_window_size()
        x1 = window_size['width'] * 0.5  # x坐标
        y1 = window_size['height'] * 0.75  # 起始y坐标
        y2 = window_size['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        """
        向下滑动屏幕
        :param t: 持续时长
        :param n: 滑动的步长
        :return:
        """
        window_size = self.driver.get_window_size()
        x1 = window_size['width'] * 0.5  # x坐标
        y1 = window_size['height'] * 0.25  # 起始y坐标
        y2 = window_size['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        """
        向左滑动屏幕
        :param t: 持续时长
        :param n: 滑动的步长
        :return:
        """
        window_size = self.driver.get_window_size()
        x1 = window_size['width'] * 0.75
        y1 = window_size['height'] * 0.5
        x2 = window_size['width'] * 0.05
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        """
        向右滑动屏幕
        :param t: 持续时长
        :param n: 滑动的步长
        :return:
        """
        window_size = self.driver.get_window_size()
        x1 = window_size['width'] * 0.05
        y1 = window_size['height'] * 0.5
        x2 = window_size['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def slideUP(self,element):
        self.wait_element(element)
        androidElement = self.find_element(element)
        x = androidElement.location['x']
        y = androidElement.location['y']
        print('y1 is',y * 0.75)
        print('y2 is',y * 0.25)
        self.driver.swipe(x, y * 0.75, x, y * 0.25, 1500);


    def switch_to_webViewOrNative(self):
        """
        native跟webview的切换
        :return:
        """
        contexts = self.driver.contexts
        current_context = self.driver.current_context
        if (contexts[0] == current_context):
            self.driver.switch_to.context(contexts[1])
            self.logger.info("切换到了:" + contexts[1])
        else:
            self.driver.switch_to.context(contexts[0])
            self.logger.info("切换到了:" + contexts[0])
            # 脚本运行失败截图

    def get_screenshot(self):
        """
        脚本运行失败截图
        :return:
        """
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        pic_path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\result\\screenshot\\" + current_date
        pic_name = current_time + '.png'
        if os.path.exists(pic_path):
            pass
        else:
            # 创建多层级的文件夹
            os.makedirs(pic_path)
        self.driver.get_screenshot_as_file(pic_path + '\\' + pic_name)
        return pic_path + '\\' + pic_name

    def quit(self):
        """
        脚本执行完毕，断开跟appium server的连接
        :return:
        """
        self.driver.quit()
