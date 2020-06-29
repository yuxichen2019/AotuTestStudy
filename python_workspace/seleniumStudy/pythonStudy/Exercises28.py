# -*- coding: utf-8 -*- 
# 2020/06/29 17:37 
# seleniumStudy
# Exercises28.py 
# company

'''有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
    问第4个人岁数，他说比第3个人大2岁。
    问第三个人，又说比第2人大两岁。
    问第2个人，说比第一个人大两岁。
    最后问第一个人，他说是10岁。请问第五个人多大？'''

def fun(n):
    if n ==1:
        return 10
    return fun(n-1)+2

print(fun(5))