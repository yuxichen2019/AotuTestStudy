# -*- coding: utf-8 -*- 
# 2020/4/11 11:52 
# seleniumStudy
# Student.py 
# company

class Student():
    def sayHello(self):
        print('Hello Python~~~~~~~~~~~~~~~~~~~~~~')

    def sum(self,begin,end):
        sum = 0
        for i in range(begin,end):
            sum = sum + i
        print(sum)

    def sum1(self,begin,end,step):
        sum = 0
        for i in range(begin,end,step):
            sum = sum + i
        print("求和结果是："+ str(sum))
        print("求和结果是：",sum)
        print("从%s----->%s的求和结果是：%s" % (begin,end,sum))
        return sum

#main方法，程序的入口
if __name__ == '__main__':
    student1=Student()  #类的实例化
    student1.sayHello() #对象 . 方法  对象调用方法。
    student1.sum(1,101)
    #偶数
    student1.sum1(300,501,2)
    #奇数
    student1.sum1(301,501,2)


