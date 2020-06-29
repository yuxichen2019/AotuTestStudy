# -*- coding: utf-8 -*- 
# 2020/06/29 17:34 
# seleniumStudy
# Exercises26.py 
# company

'''利用递归方法求5!。'''

def fun(x):
    if x == 1:
        return 1
    else:
        return fun(x-1) * x


print(fun(5))