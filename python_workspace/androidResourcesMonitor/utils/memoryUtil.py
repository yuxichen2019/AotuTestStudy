# encoding:utf-8
import os
import traceback

from PyQt4.QtCore import *
from PyQt4 import QtCore
from utils.fileUtil import FileUtil
from utils.commonUtil import CommonUtil
from utils.timeUtil import TimeUtil


class MemoryUtil(QThread):
    def __init__(self, initCount, count, packageName,resultPath):
        QThread.__init__(self)
        self.memoryTimer = QTimer(self)
        self.counter = count
        self.initCounter = initCount
        self.executeFlag = 0
        self.packageName = packageName
        self.currentData = []
        self.resultPath = resultPath
        # 注册定时任务事件
        QtCore.QObject.connect(self.memoryTimer, QtCore.SIGNAL("timeout()"), self.timeOut)

    def timeOut(self):
        self.start()

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self):
        self.start()
        self.memoryTimer.start(1000)

    # 单次测试过程
    def run(self):
        self.initCounter += self.counter
        try:
            commonUtil = CommonUtil(self.packageName,2)
            pid = commonUtil.getPid()

            memoryValue = os.popen("adb shell top -n 1 -d 0.5 | findstr " + pid)
            memoryRss=0.0
            for line in memoryValue:
                if "root" in line:
                    line = "#".join(line.split())
                    vss = line.split("#")[7].strip("K")
                    rss = line.split("#")[8].strip("K")
                    if rss:
                        memoryRss+=int(rss.strip()) /1024
            print("memoryValue is:" + str(memoryRss) + 'M')
            # 获取时间戳
            timeUtil = TimeUtil()
            currenttime = timeUtil.getCurrentTime()
            self.currentData.append([currenttime, memoryRss])
            # 保存文件
            fileUtil = FileUtil(self.resultPath, self.currentData)
            fileUtil.saveDataToCSV()
        except:
            traceback.print_exc()
        self.emit(SIGNAL("output(QString,QString)"),str(self.initCounter),str(memoryRss))


if __name__ == "__main__":
    memoryUtil = MemoryUtil(100, 10,"com.tencent.mm","D:\\tmp")
    #memoryUtil.executeCommand()
    #print(memoryUtil.executeFlag)
    print(memoryUtil.run())