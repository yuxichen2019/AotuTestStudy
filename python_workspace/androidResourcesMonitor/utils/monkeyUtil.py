# encoding:utf-8
import subprocess
import traceback

from PyQt4.QtCore import *
from utils.timeUtil import TimeUtil
from utils.fileUtil import FileUtil

class MonkeyUtil(QThread):
    def __init__(self, monkeyParameter,logPath):
        QThread.__init__(self)
        self.monkeyParameter = monkeyParameter
        self.logPath = logPath

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self):
        self.start()

    # 单次测试过程
    def run(self):
        # 获取日志文件
        timeUtil = TimeUtil()
        currentDateAndTime = timeUtil.getCurrentDateAndTime()
        self.logFile=self.logPath+"\\"+currentDateAndTime+".txt";
        try:
            popen = subprocess.Popen("adb shell monkey -p " + self.monkeyParameter, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            while True:
                # 获取当前grep出来的日志文本行
                line = popen.stdout.readline().strip()
                if not line:
                    # 测试执行完毕，发送消息解析日志
                    self.emit(SIGNAL("output(QString,QString)"), str(self.logFile),"true")
                    break
                # 异步日志数据发送到前端
                self.emit(SIGNAL("output(QString)"), str(line))
                # 日志文件写到本地
                # 保存文件
                fileUtil = FileUtil(self.logFile,timeUtil.getCurrentLogDateAndTime()+":"+str(line))
                fileUtil.saveDataToTXT()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    MonkeyUtil = MonkeyUtil("com.eclite.activity --pct-touch 70 --pct-motion 0 --pct-appswitch 30 --pct-rotation 0 -v -v -v 3000","D:")
    print(MonkeyUtil.run())
