#!/usr/bin/python3

# 定义类
class Student:

    # 定义属性
    name = ''
    age = ''
    classNo = ''
    hobby = ''
    counterResult = 0
    counterResult1 = 0
    counterResult2 = 0

    # 打印Hello World
    def printHello(self):
        print("hello python")

    def counterNew(self):
        result1=0
        result2=0
        for i in range(1, 100):
            if (i % 2 == 0):
                result1 = result1 + i
            else:
                result2 = result2 + i
        print("累加奇数和的结果是：", result2)
        print("累加偶数和的结果是：", result1)

    def counter2(self, startNo, endNo, no):
        for i in range(startNo, endNo):
            if (i % no == 0):
                self.counterResult1 = self.counterResult1 + i
            else:
                self.counterResult2 = self.counterResult2 + i
        print("累加奇数和的结果是：", self.counterResult2)
        print("累加偶数和的结果是：" + str(self.counterResult1))


    # 定义构造方法
    def __init__(self, name, age, classNo, hobby):
        self.name = name
        self.age = age
        self.classNo = classNo
        self.hobby = hobby

    # def __init__(self):
    #     print("这是一个空的构造方法")

    def speak(self):
        print("这里是说话方法")
        print("name:%s  age:%d classNo:%s hobby:%s" % (self.name, self.age, self.classNo, self.hobby))

    def walk(self):
        print("这里是走路方法")
        print("我要去买iphonex")

    def counter(self):
        for i in range(1, 100):
            self.counterResult = self.counterResult + i
        print("累加求和的结果是：" + str(self.counterResult))

    def counter(self):
        result=0
        for i in range(1, 100):
            result = result + i
        print("累加求和的结果是：" + str(result))


    def counter1(self, startNo, endNo):
        for i in range(startNo, endNo):
            if (i % 2 == 0):
                self.counterResult1 = self.counterResult1 + i
            else:
                self.counterResult2 = self.counterResult2 + i
        print("累加奇数和的结果是：", self.counterResult2)
        print("累加偶数和的结果是：" + str(self.counterResult1))

    def counter2(self,starNo,endNo):
        for i in range(starNo, endNo):
            if (i % 2 == 0):
                self.counterResult1 = self.counterResult1 + i
            else:
                self.counterResult2 = self.counterResult2 + i
        print("累加奇数和的结果是：", self.counterResult2)
        print("累加偶数和的结果是：" + str(self.counterResult1))

    def counter2(self, startNo, endNo, no):
        for i in range(startNo, endNo):
            if (i % no == 0):
                self.counterResult1 = self.counterResult1 + i
            else:
                self.counterResult2 = self.counterResult2 + i
        print("累加奇数和的结果是：", self.counterResult2)
        print("累加偶数和的结果是：" + str(self.counterResult1))


if __name__ == '__main__':
    ligang = Student()
    ligang.sayHello()
    ligang = Student("李刚", 22, "1班", "王者荣耀")
    print("我的姓名是:",ligang.name)
    print("我的年龄是:",ligang.age)
    print("我的班级是",ligang.classNo)
    print("我的爱好是",ligang.hobby)
    ligang.counter1(1,100)
    # student = Student()
    ligang.speak()
    ligang.walk()
    # student.counter2(1, 100, 5)
    # ligang.counter(1, 101)
    # ligang.counter1(1, 101)


