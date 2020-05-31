# encoding:utf-8


import time


class TimeUtil(object):

    # 获取当前系统时间
    def getCurrentTime(self):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        return currentTime

    # 获取当前系统日期和时间
    def getCurrentDateAndTime(self):
        currentDateAndTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        return currentDateAndTime

    # 获取当前系统日期和时间
    def getCurrentLogDateAndTime(self):
        currentDateAndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentDateAndTime

if __name__ == "__main__":
    timeUtil = TimeUtil()
    print(timeUtil.getCurrentTime())
    print(timeUtil.getCurrentDateAndTime())
