# -*- coding: utf-8 -*- 
# 2020/05/26 11:32 
# seleniumStudy
# Exercises15.py 
# company

'''利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'''

num = int(input('请输入学生成绩'))
if num >= 90:
    print('A')
else:
    if num >= 60:
        print('B')
    else:
        print('C')