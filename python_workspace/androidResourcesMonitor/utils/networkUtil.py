# encoding:utf-8
import os
import traceback

from PyQt4.QtCore import *
from PyQt4 import QtCore
from utils.commonUtil import CommonUtil
from utils.fileUtil import FileUtil
from utils.timeUtil import TimeUtil


class NetworkUtil(QThread):
    def __init__(self, initCount, count, packageName,resultPath):
        QThread.__init__(self)
        self.netWorkTimer = QTimer(self)
        self.counter = count
        self.initCounter = initCount
        self.executeFlag = 0
        self.packageName = packageName
        self.currentData = []
        self.resultPath = resultPath
        # 注册定时任务事件
        QtCore.QObject.connect(self.netWorkTimer, QtCore.SIGNAL("timeout()"), self.timeOut)

    def timeOut(self):
        self.start()

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self):
        self.start()
        self.netWorkTimer.start(1000)

    def run(self):
        # 执行获取进程的命令
        alltraffic=0
        try:
            # 获取进程ID
            commonUtil = CommonUtil(self.packageName,2)
            pid = commonUtil.getPid()
            # 获取进程ID使用的流量
            executeResult = os.popen("adb shell cat /proc/" + pid + "/net/dev | findstr wlan0")
            if executeResult:
                networkValue = "#".join(executeResult.readline().split())
                receive = networkValue.split("#")[1]
                transmit = networkValue.split("#")[9]
                alltraffic = int(receive) + int(transmit)
            # 按MB计算流量值
            alltraffic = alltraffic / (1024 * 1024)
            # 获取时间戳
            timeUtil = TimeUtil()
            currenttime = timeUtil.getCurrentTime()
            self.currentData.append([currenttime, alltraffic])
            # 保存文件
            fileUtil = FileUtil(self.resultPath, self.currentData)
            fileUtil.saveDataToCSV()
        except:
            traceback.print_exc()
        self.emit(SIGNAL("output(QString,QString)"),str(self.initCounter),str(alltraffic))

# if __name__ == "__main__":
#     networkUtil = NetworkUtil(100, 10)
#     networkUtil.executeCommand()
