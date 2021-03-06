import os
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from framework.Logger import Logger


class BlueRose:
    def logging(func):
        logger = Logger('blueRose.log', level='debug').logger
        def wrapper(*args, **kwargs):
            if (args.__len__() > 1):
                logger.info(func.__name__ + ' has been executed for element ' + args[1])
            else:
                logger.info(func.__name__ + ' has been executed')
            return func(*args, **kwargs)

        return wrapper

    """
        BlueRose framework are committed to a simpler automated testing,based on the original selenium.
    """

    @logging
    def __init__(self, browser='firefox', isMultitask=False):
        self.logger = Logger('blueRose.log', level='debug').logger
        self.seconds=30
        # 存储错误截图的列表
        self.imgs=[]
        if isMultitask:
            self.initMultitaskDriver(browser, serverUrl='http://127.0.0.1:4444/wd/hub')
        else:
            self.initDriver(browser)

    @logging
    def initDriver(self, browser='firefox'):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        运行类初始化方法，默认为驱动Firefox，也可以设置谷歌 ie
        """
        try:
            if browser == "firefox":
                self.driver = webdriver.Firefox()
            elif browser == "chrome":
                self.driver = webdriver.Chrome()
            elif browser == "ie":
                self.driver = webdriver.Ie()
            self.driver.implicitly_wait(5)
        except Exception:
           self.logger.error("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")
           assert False

    @logging
    def initMultitaskDriver(self, browser='chrome', serverUrl='http://localhost:4444/wd/hub'):
        """
        Run class initialization method for multitask, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        多任务运行类初始化方法。。
        """
        try:
            if browser == "firefox":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.FIREFOX)
            elif browser == "chrome":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.CHROME)
            elif browser == "ie":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            self.driver.implicitly_wait(5)
        except Exception:
            self.logger.error("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")
            assert False

    @logging
    def get(self, url):
        """
        Open url,same as get.
        打开url，与get相同。
        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)

    @logging
    def max_window(self):
        """
        Set browser window maximized.
        设置浏览器窗口最大化。
        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    @logging
    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.
        设置浏览器窗口的长宽
        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    @logging
    def wait(self, secsonds):
        """
        Implicitly wait.All elements on the page.
        隐式等待。页面上的所有元素。
        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    @logging
    def find_element(self, element):
        """
        Judge element positioning way, and returns the element.
        判断元素定位方式，返回元素。
        Usage:
        driver.find_element("id=kw")
        """
        if "=" not in element:
            self.logger.error("SyntaxError: invalid syntax, lack of '='.")
            assert False
        else:
            try:
                by = element[0: element.find("=")]
                value = element[element.find("=") + 1: len(element)]

                if by == "id":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.ID, value)))
                    return self.driver.find_element_by_id(value)
                elif by == "name":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.NAME, value)))
                    return self.driver.find_element_by_name(value)
                elif by == "class":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, value)))
                    return self.driver.find_element_by_class_name(value)
                elif by == "text":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.LINK_TEXT, value)))
                    return self.driver.find_element_by_link_text(value)
                elif by == "xpath":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.XPATH, value)))
                    return self.driver.find_element_by_xpath(value)
                elif by == "css":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                    return self.driver.find_element_by_css_selector(value)
                else:
                    self.logger.error("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
                    assert False
            except Exception:
                self.imgs.append(self.driver.get_screenshot_as_base64())
                self.logger.exception("Time out can not find the element,the screen shot is:" + self.get_screenshot())
                assert False

    @logging
    def find_elements(self, element, index):
        """
        Judge element positioning way and index, and returns the element.
        判断元素的定位方式和索引，返回元素。
        Usage:
        driver.find_element("id=kw",1)
        """
        if "=" not in element:
            self.logger.error("SyntaxError: invalid syntax, lack of '='.")
            assert False
        else:
            try:
                by = element[0: element.find("=")]
                value = element[element.find("=") + 1:len(element)]

                if by == "id":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.ID, value)))
                    return self.driver.find_elements_by_id(value)[index]
                elif by == "name":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.NAME, value)))
                    return self.driver.find_elements_by_name(value)[index]
                elif by == "class":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, value)))
                    return self.driver.find_elements_by_class_name(value)[index]
                elif by == "text":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.LINK_TEXT, value)))
                    return self.driver.find_elements_by_link_text(value)[index]
                elif by == "xpath":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.XPATH, value)))
                    return self.driver.find_elements_by_xpath(value)[index]
                elif by == "css":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                    return self.driver.find_elements_by_css_selector(value)[index]
                elif by == "tagName":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.TAG_NAME, value)))
                    return self.driver.find_elements_by_tag_name(value)[index]
                else:
                    self.logger.error("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
                    assert False
            except Exception:
                self.logger.exception("Time out can not find the element,the screen shot is:" + self.get_screenshot())
                assert False

    @logging
    def send_keys(self, element, text):
        """
        Operation input content after clear.
        清除后操作输入内容。
        Usage:
        driver.send_keys("id=kw","selenium")
        """
        element=self.find_element(element)
        element.clear()
        element.send_keys(text)

    @logging
    def send_keyBoardsEvent(self, element, keyEvent):
        """
        Operation send key board event on target.
        操作发送目标上的键盘事件。
        Usage:
        driver.send_keyBoardsEvent("id=kw","Keys.ENTER")
        """
        self.find_element(element).send_keys(keyEvent)

    @logging
    def send_keys_index(self, element, index, text):
        """
        Operation input content after clear.
        清除后操作输入内容。
        Usage:
        driver.send_keys_index("id=kw",5,"selenium")
        """
        element=self.find_elements(element, index)
        element.clear()
        element.send_keys(text)

    @logging
    def click(self, element):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        它可以点击任何可以点击的文本/图像，连接、复选框、单选按钮，甚至下拉框等。。
        Usage:
        driver.click("id=kw")
        """
        self.find_element(element).click()

    @logging
    def click_index(self, element, index):
        """
        It can click any text / image can be clicked
        它可以点击任何可以点击的文本/图像
        Usage:
        driver.click_index("id=kw",5)
        """
        self.find_elements(element, index).click()

    @logging
    def right_click(self, element):
        """
        Right click element.
        右击
        Usage:
        driver.right_click("class=right")
        """
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    @logging
    def move_to_element(self, element):
        """
        Mouse over the element.
        鼠标移动到元素上面
        Usage:
        driver.move_to_element("css=choose")
        """
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    @logging
    def double_click(self, element):
        """
        Double click element.
        双击
        Usage:
        driver.double_click("name=baidu")
        """
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    @logging
    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.
        将一个元素拖到一定的距离，然后将其放下
        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                self.find_element(target_element)).perform()

    @logging
    def back(self):
        """
        Back to old window.
        回退到旧窗口
        Usage:
        driver.back()
        """
        self.driver.back()

    @logging
    def forward(self):
        """
        Forward to old window.
        前进到老窗口。
        Usage:
        driver.forward()
        """
        self.driver.forward()

    @logging
    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.
        获取元素属性的值。
        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        return self.find_element(element).get_attribute(attribute)

    # @logging
    # def get_cur_windowhandle(self):
    #     """
    #     Get current window handle
    #     获取当前窗口的句柄
    #     """
    #     return self.driver.current_window_handle
    #
    # @logging
    # def get_all_windowhandle(self):
    #     """
    #     Returns the handle of all windows to the current session
    #     将所有窗口的句柄返回到当前会话
    #     """
    #     return self.driver.window_handles
    #
    # @logging
    # def switch_to_window(self,handles):
    #     """
    #     Switch to the corresponding window
    #     切换到相应的窗口
    #     """
    #     return self.driver.switch_to.window(handles)



    @logging
    def get_text(self, element):
        """
        Get element text information.
        获取元素文本信息。
        Usage:
        driver.get_text("name=johnny")
        """
        return self.find_element(element).text

    @logging
    def get_display(self, element):
        """
        Gets the element to display,The return result is true or false.
        获取要显示的元素，返回结果为true或false。
        Usage:
        driver.get_display("id=ppp")
        """
        return self.find_element(element).is_displayed()

    @logging
    def get_title(self):
        """
        Get window title.
        获取窗口标题。
        Usage:
        driver.get_title()
        """
        return self.driver.title

    @logging
    def get_url(self):
        """
        Get the URL address of the current page.
        获取当前页面的URL
        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    @logging
    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64()

    @logging
    def get_screenshot(self):
        """
        Get the current window screenshot.
        截屏
        Usage:
        driver.get_screenshot()
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

    @logging
    def submit(self, element):
        """
        Submit the specified form.
        提交指定的表格。
        Usage:
        driver.submit("id=mainFrame")
        """
        self.find_element(element).submit()

    @logging
    def switch_to_frame(self, element):
        """
        Switch to the specified frame.
        切换到指定的frame
        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.driver.switch_to.frame(self.find_element(element))

    @logging
    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        返回上一级的当前窗体计算机窗体。
        与switch_to_frame（）方法的对应关系。
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.parent_frame()

    @logging
    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        与switch_to_frame（）方法的对应关系。
        Usage:
        driver.switch_to_default()
        """
        self.driver.switch_to.default_content()

    @logging
    def open_new_window(self):
        """
        Open the new window and switch the handle to the newly opened window.
        打开新窗口并将手柄切换到新打开的窗口。
        Usage:
        driver.open_new_window()
        """
        current_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def F5(self):
        '''
        Refresh the current page.
        刷新
        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    @logging
    def js(self, script):
        """
        Execute JavaScript scripts.
        执行JavaScript脚本。
        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        Accept warning box.
        接受警告框。
        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        解除可用的警报。
        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        Close the windows.
        关闭窗口
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        退出驱动程序并关闭所有窗口。
        Usage:
        driver.quit()
        """
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    # from BlueRose import BlueRose
    # driver = BlueRose("chrome")  # 调用浏览器，支持 'firefox', 'chrome', 'ie' or 'phantomjs'
    driver = BlueRose(browser="chrome")
    driver.get("http://www.baidu.com")
    driver.max_window()  # 浏览器最大化
    driver.send_keys("id=kw", "selenium")  # 该元素位置输入内容
    time.sleep(2)
    driver.click("id=su")
    time.sleep(2)
    driver.click("id=result_logo")  # 点击元素
    time.sleep(2)
    driver.F5()  # 刷新页面
    driver.get_screenshot()  # 截图
    time.sleep(2)
    driver.back()  # 后退
    time.sleep(2)
    driver.forward()  # 前进
    driver.close()
