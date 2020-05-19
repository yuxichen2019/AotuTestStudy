import datetime
import time


class UtilsDate(object):

    # 获取系统日期和时间
    @staticmethod
    def getCurrentDateAndTime():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 获取系统日期
    @staticmethod
    def getCurrentDate():
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 获取系统时间
    @staticmethod
    def getCurrentTime():
        return time.strftime("%H:%M:%S", time.localtime(time.time()))

    # 获取时间戳
    @staticmethod
    def getTimeStamp():
        return (int(round(time.time() * 1000)))

    # 获取当前日期后几天
    @staticmethod
    def getOverTime(days):
        return (datetime.date.today() + datetime.timedelta(days=days)).strftime('%Y-%m-%d');

if __name__ == '__main__':
    print("当前系统日期和时间："+UtilsDate.getCurrentDateAndTime())
    print("当前系统日期："+UtilsDate.getCurrentDate())
    print("当前系统时间："+UtilsDate.getCurrentTime())
