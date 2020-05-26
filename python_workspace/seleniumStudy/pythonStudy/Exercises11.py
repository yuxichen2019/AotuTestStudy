# -*- coding: utf-8 -*- 
# 2020/05/25 16:31 
# seleniumStudy
# Exercises11.py 
# company


'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1 1 2 3 5 8 13 21 34  55
'''

def fun(n):
    if n == 1 or n == 2:
        result=1
    else:
        result = fun(n-1) + fun(n-2)
    return result
aa=fun(10)
print(aa)


