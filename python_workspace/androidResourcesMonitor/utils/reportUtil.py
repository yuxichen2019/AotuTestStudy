# encoding:utf-8


import re
from utils.fileUtil import FileUtil
# from fileUtil import FileUtil


class ReportUtil(object):
    # 异常类型
    # 1空指针异常
    NullPointerException="java.lang.NullPointerException"
    NullPointerExceptionCounter=0
    # 2数组溢出
    ArrayIndexOutOfBoundsException="java.lang.ArrayIndexOutOfBoundsException"
    ArrayIndexOutOfBoundsExceptionCounter=0
    # 3类不存在
    ClassNotFoundException="java.lang.ClassNotFoundException"
    ClassNotFoundExceptionCounter=0
    # 4数学运算异常
    ArithmeticException="java.lang.ArithmeticException"
    ArithmeticExceptionCounter=0
    # 5方法参数异常
    IllegalArgumentException="java.lang.IllegalArgumentException"
    IllegalArgumentExceptionCounter=0
    # 6文件未找到
    FileNotFoundException="java.lang.FileNotFoundException"
    FileNotFoundExceptionCounter=0
    # 7数值转化异常
    NumberFormatException="java.lang.NumberFormatException"
    NumberFormatExceptionCounter=0
    # 8堆栈异常错误
    StackOverflowError="java.lang.StackOverflowError"
    StackOverflowErrorCounter=0
    # 9内存溢出错误
    OutOfMemoryError="java.lang.OutOfMemoryError"
    OutOfMemoryErrorCounter=0

    def __init__(self, filePath):
        self.filePath = filePath
        # 存储报告的三维数组
        self.currentData =[]

    # 解析日志中的错误信息
    def analysisLog(self,flag):
        if flag:
            fileUtil = FileUtil(self.filePath,"")
            allDataRows=fileUtil.readDataFromTXT()
            for row in allDataRows:
                if re.findall(self.NullPointerException,row):
                    self.NullPointerExceptionCounter=self.NullPointerExceptionCounter+1
                if re.findall(self.ArrayIndexOutOfBoundsException,row):
                    self.ArrayIndexOutOfBoundsExceptionCounter=self.ArrayIndexOutOfBoundsExceptionCounter+1
                if re.findall(self.ClassNotFoundException,row):
                    self.ClassNotFoundExceptionCounter=self.ClassNotFoundExceptionCounter+1
                if re.findall(self.ArithmeticException,row):
                    self.ArithmeticExceptionCounter=self.ArithmeticExceptionCounter+1
                if re.findall(self.IllegalArgumentException,row):
                    self.IllegalArgumentExceptionCounter=self.IllegalArgumentExceptionCounter+1
                if re.findall(self.FileNotFoundException,row):
                    self.FileNotFoundExceptionCounter=self.FileNotFoundExceptionCounter+1
                if re.findall(self.NumberFormatException,row):
                    self.NumberFormatExceptionCounter=self.NumberFormatExceptionCounter+1
                if re.findall(self.StackOverflowError,row):
                    self.StackOverflowErrorCounter=self.StackOverflowErrorCounter+1
                if re.findall(self.OutOfMemoryError,row):
                    self.OutOfMemoryErrorCounter=self.OutOfMemoryErrorCounter+1
        # 装载测试报告的三维数组
        self.currentData.append([self.NullPointerException,self.NullPointerExceptionCounter,"空指针异常"])
        self.currentData.append([self.ArrayIndexOutOfBoundsException,self.ArrayIndexOutOfBoundsExceptionCounter,"数组溢出"])
        self.currentData.append([self.ClassNotFoundException,self.ClassNotFoundExceptionCounter,"类不存在"])
        self.currentData.append([self.ArithmeticException,self.ArithmeticExceptionCounter,"数学运算异常"])
        self.currentData.append([self.IllegalArgumentException,self.IllegalArgumentExceptionCounter,"方法参数异常"])
        self.currentData.append([self.FileNotFoundException,self.FileNotFoundExceptionCounter,"文件未找到"])
        self.currentData.append([self.NumberFormatException,self.NumberFormatExceptionCounter,"数值转化异常"])
        self.currentData.append([self.StackOverflowError,self.StackOverflowErrorCounter,"堆栈异常错误"])
        self.currentData.append([self.OutOfMemoryError,self.OutOfMemoryErrorCounter,"内存溢出错误"])
        return self.currentData

if __name__ == "__main__":
    reportUtil = ReportUtil("E:\\pythonWorkSpace\\androidSourceMonitor\\ouput\\2017-05-17-10-49-19.txt")
    print(reportUtil.analysisLog(True))
