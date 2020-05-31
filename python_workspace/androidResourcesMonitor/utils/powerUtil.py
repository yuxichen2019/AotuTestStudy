# encoding:utf-8
import os
import traceback

from PyQt4.QtCore import *
from PyQt4 import QtCore
from utils.fileUtil import FileUtil
from utils.timeUtil import TimeUtil


class PowerUtil(QThread):
    def __init__(self, initCount, count,resultPath):
        QThread.__init__(self)
        self.powerTimer = QTimer(self)
        self.counter = count
        self.initCounter = initCount
        self.executeFlag = 0
        self.currentData = []
        self.resultPath = resultPath
        # 注册定时任务事件
        QtCore.QObject.connect(self.powerTimer, QtCore.SIGNAL("timeout()"), self.timeOut)

    def timeOut(self):
        self.start()

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self):
        self.start()
        self.powerTimer.start(1000)

    # 单次测试过程
    def run(self):
        self.initCounter += self.counter
        # 设备修改为非充电状态
        os.popen("adb shell dumpsys battery set status 1")
        powerValue=0
        try:
            result = os.popen("adb shell dumpsys battery |findstr level")
            powerValue = result.readline().split(":")[1].strip()
            # 获取时间戳
            timeUtil = TimeUtil()
            currenttime = timeUtil.getCurrentTime()
            self.currentData.append([currenttime, powerValue])
            # 保存文件
            fileUtil = FileUtil(self.resultPath, self.currentData)
            fileUtil.saveDataToCSV()
        except:
            traceback.print_exc()
        self.emit(SIGNAL("output(QString,QString)"),str(self.initCounter),str(powerValue))

# if __name__ == "__main__":
#     powerUtil = PowerUtil(100, 10)
#     powerUtil.executeCommand()
