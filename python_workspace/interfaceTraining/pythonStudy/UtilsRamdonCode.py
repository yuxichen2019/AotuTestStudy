# -*-coding:utf-8 -*-
import random
import time


class RamdonCode(object):

    def getCurrentDate(self):
        return time.strftime("%Y%m%d", time.localtime(time.time()))

    def getNo(self,count):
        return "".join(random.choice("0123456789") for i in range(count))


    def getRamdonCode(self):
        busniessCode = self.getCurrentDate() + "-" + self.getNo(4)
        print(busniessCode)
        return busniessCode


if __name__ == "__main__":
    a = RamdonCode()
    a.getRamdonCode()


