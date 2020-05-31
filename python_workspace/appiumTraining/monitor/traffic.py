# /usr/bin/python
# encoding:utf-8
import csv
import os
import time


# 控制类
class MonitoringTrafficResources(object):
    def __init__(self, count):
        # 定义测试的次数
        self.counter = count
        # 定义收集数据的数组
        self.alldata = [("timestamp", "traffic")]

    # 单次测试过程
    def testprocess(self):
        # 执行获取进程的命令
        result = os.popen("adb shell ps | findstr com.tencent.mm")
        # 获取进程ID
        pidLine=result.readlines()[0]
        pidStr = "#".join(pidLine.split())
        print("pidStr is:"+pidStr)
        pid = pidStr.split("#")[2]
        print("pid is:" + pid)
        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
        for line in traffic:
            if "wlan0" in line:
                # 将所有空行换成#
                line = "#".join(line.split())
                # 按#号拆分,获取收到和发出的流量
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
                # elif "eth1" in line:
                #     # 将所有空行换成#
                #     line = "#".join(line.split())
                #     # 按#号拆分,获取收到和发出的流量
                #     receive2 = line.split("#")[1]
                #     transmit2 = line.split("#")[9]

        # 计算所有流量的之和
        # alltraffic = string.atoi(receive) + string.atoi(transmit) + string.atoi(receive2) + string.atoi(transmit2)
        # alltraffic = receive + transmit + receive2 + transmit2
        alltraffic = float(receive) + float(transmit)
        # 按M计算流量值
        alltraffic = float(alltraffic) / (1024*1024)
        # 获取当前时间
        currenttime = self.getCurrentTime()
        # 将获取到的数据存到数组中
        print("currenttime is:"+currenttime)
        print("alltraffic is:"+ str('%.2f' % (alltraffic)) + ' M')
        self.alldata.append((currenttime, alltraffic))

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
        csvfile = open('./result/traffic.csv', 'w', encoding='utf8', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    monitoringTrafficResources = MonitoringTrafficResources(50)
    monitoringTrafficResources.run()
    monitoringTrafficResources.SaveDataToCSV()
