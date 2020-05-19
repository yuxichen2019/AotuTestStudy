import win32gui
from time import sleep
import win32con
from ddt import ddt, data, unpack
from testCase.crm.BaseCase import BaseCase


@ddt
class TestUploadFileForCustomer(BaseCase):

    @data(['15112342277','yxc253676'],
          ['19926451606','ujm159yhn753'])
    @unpack
    def test_uploadFile(self,username,password):

        self.login(self,username,password)
        # 打开客户管理
        self.driver.click("xpath=//span[contains(text(),'客户管理')]")
        # 点击客户管理列表下的客户
        self.driver.click("xpath=//a[contains(@href,'/index.php?m=customer&a=index&by=me')]")
        # 点击操作
        self.driver.click("xpath=//button[@data-toggle='dropdown']")
        # 点击导入文件
        self.driver.click("id=import_excel")
        # 点击选择文件
        sleep(1)
        self.driver.js(
            "document.getElementById('file').click()")
        sleep(1)
        # os.system(r"E:\python-workSpace\seleniumTraining\autoIt\upload.exe")
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", "打开")
        sleep(3)
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级

        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # 输入文件的绝对路径，点击“打开”按钮
        file_path=r"E:\python-workSpace\seleniumTraining\autoIt\ces.xls"
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        sleep(6)
        self.driver.click("xpath=(//span[text()='确定' and @class='ui-button-text'])[4]")