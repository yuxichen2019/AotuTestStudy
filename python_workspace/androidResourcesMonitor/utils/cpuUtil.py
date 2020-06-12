# encoding:utf-8
import os
import traceback
from PyQt4 import QtCore
from PyQt4.QtCore import *
from utils.fileUtil import FileUtil
from utils.timeUtil import TimeUtil


class CpuUtil(QThread):
    def __init__(self, initCount, count, packageName,resultPath):
        QThread.__init__(self)
        self.cpuTimer = QTimer(self)
        self.counter = count
        self.initCounter = initCount
        self.executeFlag = 0
        self.packageName = packageName
        self.currentData =[]
        self.resultPath=resultPath
        # 注册定时任务事件
        QtCore.QObject.connect(self.cpuTimer, QtCore.SIGNAL("timeout()"), self.timeOut)

    def timeOut(self):
        self.start()

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self):
        self.start()
        self.cpuTimer.start(1000)

    # 单次测试过程
    def run(self):
        self.initCounter += self.counter
        print("adb shell dumpsys cpuinfo | findstr " + self.packageName)
        result = os.popen("adb shell dumpsys cpuinfo | findstr " + self.packageName)
        cpuvalue=0.0
        try:
            for line in result:
                cpuLine1 = line.split("%")[0].strip()
                print("line.strip() is:"+cpuLine1)
                if cpuLine1:
                    cpuvalue+=float(cpuLine1)
            print("cpu value is:"+str(cpuvalue))
            # 获取时间戳
            timeUtil=TimeUtil()
            currenttime = timeUtil.getCurrentTime()
            self.currentData.append([currenttime, cpuvalue])
            # 保存文件
            fileUtil=FileUtil(self.resultPath,self.currentData)
            fileUtil.saveDataToCSV()
        except:
            traceback.print_exc()
        self.emit(SIGNAL("output(QString,QString)"),str(self.initCounter),str(cpuvalue))

if __name__ == "__main__":
    CpuUtil = CpuUtil(100, 10,"com.tencent.mm","D:\\tmp")
    print(CpuUtil.run())
    #CpuUtil.run()