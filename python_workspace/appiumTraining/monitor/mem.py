# /usr/bin/python
# encoding:utf-8
import csv
import os
import time


# 控制类
class MonitoringMemResources(object):
    def __init__(self, count):
        # 定义测试的次数
        self.counter = count
        # 定义收集数据的数组
        self.alldata = [("timestamp", "rss")]

    # # 单次测试过程
    # def testprocess(self):
    #     # 执行获取进程的命令
    #     result = os.popen("adb shell ps | findstr com.tencent.mm")
    #     # 获取进程ID
    #     # pid = result.readlines()[0].split(" ")[5]
    #     pidLine = result.readlines()[0]
    #     pidStr = "#".join(pidLine.split())
    #     print("pidStr is:" + pidStr)
    #     pid = pidStr.split("#")[2]
    #     print("pid is:" + pid)
    #     # 获取进程ID使用的流量
    #     traffic = os.popen("adb shell top -n 1 -d 0.5 | findstr " + pid)
    #
    #     for line in traffic:
    #         if "root" in line:
    #             line = "#".join(line.split())
    #             print(line)
    #             vss = line.split("#")[7].strip("K")
    #             rss = line.split("#")[8].strip("K")
    #     currenttime = self.getCurrentTime()
    #     print("current time is:"+currenttime)
    #     print("vss used is:"+vss+' K')
    #     print("rss used is:"+rss+' K')
    #     # 将获取到的数据存到数组中
    #     self.alldata.append((currenttime, int(rss) / 1024))


    # 累加内存
    def testprocess(self):
        # 执行获取进程的命令
        result = os.popen("adb shell ps | findstr com.tencent.mm")
        # 获取进程ID
        # pid = result.readlines()[0].split(" ")[5]
        pidLine = result.readlines()[0]
        pidStr = "#".join(pidLine.split())
        print("pidStr is:" + pidStr)
        pid = pidStr.split("#")[2]
        print("pid is:" + pid)
        # 获取进程ID使用的内存
        traffic = os.popen("adb shell top -n 1 -d 0.5 | findstr " + pid)

        vss=0.0
        rss=0.0
        for line in traffic:
            if "root" in line:
                line = "#".join(line.split())
                print(line)
                vss1 = line.split("#")[7].strip("K")
                rss1 = line.split("#")[8].strip("K")
                vss+=float(vss1)
                rss+=float(rss1)

        currenttime = self.getCurrentTime()
        print("current time is:"+currenttime)
        print("vss used is:"+str(vss/1024)+' M')
        print("rss used is:"+str(rss/1024)+' M')
        # 将获取到的数据存到数组中
        self.alldata.append((currenttime, int(rss) / 1024))


    # 多次测试过程控制
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            # 每5秒钟采集一次数据
            time.sleep(5)

    # 获取当前的时间戳
    def getCurrentTime(self):
        # currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = open('./result/meminfo.csv', 'w', encoding='utf8', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    monitoringMemResources = MonitoringMemResources(50)
    monitoringMemResources.run()
    monitoringMemResources.SaveDataToCSV()
