# -*- coding: utf-8 -*- 
# 2020/06/29 17:37 
# seleniumStudy
# Exercises27.py 
# company


'''利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。'''



def fun(s,l):

    if l == 0:
        return
    print(s[l-1],end=' ')
    fun(s,l-1)


s=input('请输入一个字符串:')
l = len(s)
fun(s,l)