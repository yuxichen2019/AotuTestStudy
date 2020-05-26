# -*- coding: utf-8 -*- 
# 2020/05/25 16:50 
# seleniumStudy
# Exercises12.py 
# company


'''
101-200之间的素数有多少个，并打印出来
'''
from math import sqrt
list=[]

for i in range(101,201):
    a = int(sqrt(i))
    for j in range(2,a+1):
        if i % j == 0:
            break
        else:
            if j == a:
                list.append(i)

# for k in range(101,201):
#     if k not in list:
#         list.append(k)
#     else:
#         list.remove(k)
print(len(list))
print(list)