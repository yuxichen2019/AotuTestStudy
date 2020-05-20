# -*- coding: utf-8 -*- 
# 2020/05/20 12:01 
# seleniumStudy
# Ranking_of_students_scores.py 
# company


''' 请设计一个学生类，学生包含两个属性姓名与成绩，请用java或python实现学生成绩的降序排列，并计算学生成绩的总和。'''



class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def getname(self):
        return self.name

    def getscore(self):
        return self.score


if __name__ == '__main__':
    s1=Student('张三',99)
    s2=Student('李四',66)
    s3=Student('王五',77)
    s4=Student('孙六',88)
    s5=Student('赵七',55)
    list=[s1,s2,s3,s4,s5]

    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j].getscore() > list[j+1].getscore():
                continue
            else:
                tmp=list[j]
                list[j] = list[j+1]
                list[j+1]=tmp

    dict={}
    for i in list:
        dict[i.getname()]=i.getscore()
    print(dict)


