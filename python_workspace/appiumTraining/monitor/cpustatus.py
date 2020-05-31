# /usr/bin/python
# encoding:utf-8
import csv
import os
import time


# 监控CPU资源信息
class MonitoringCPUResources(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "cpustatus")]


    # 单次执行监控过程(累加)
    def monitoring(self):
        result = os.popen("adb shell dumpsys cpuinfo | findstr com.tencent.mm")
        cpuvalue=0.0
        for line in result:
            cpuvalue1 =line.split("%")[0].strip()
            cpuvalue=cpuvalue+float(cpuvalue1)
        currenttime = self.getCurrentTime()
        print("current time is:" + currenttime)
        print("cpu used is:" + str(cpuvalue))
        self.alldata.append([currenttime, cpuvalue])


    # 多次执行监控过程
    def run(self):
        while self.counter > 0:
            self.monitoring()
            self.counter = self.counter - 1
            time.sleep(3)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = open('./result/cpustatus.csv', 'w', encoding='utf8', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    monitoringCPUResources = MonitoringCPUResources(100)
    monitoringCPUResources.run()
    monitoringCPUResources.SaveDataToCSV()
