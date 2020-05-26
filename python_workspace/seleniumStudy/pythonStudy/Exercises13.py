# -*- coding: utf-8 -*- 
# 2020/05/25 17:28 
# seleniumStudy
# Exercises13.py 
# company


'''
打印出100-999之间的所有水仙花数
指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身。如371 = 3^3 + 7^3+ 1^3，则371是一个水仙花数。
'''

list=[]
for i in range(101,1000):
    a= int(i/100)
    b=(int(i/10))%10
    c=i%10
    if a**3 + b**3 + c**3 == i:
        list.append(i)

print(list)