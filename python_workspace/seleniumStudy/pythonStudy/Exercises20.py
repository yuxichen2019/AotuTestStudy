# -*- coding: utf-8 -*- 
# 2020/05/29 17:29 
# seleniumStudy
# Exercises20.py 
# company


'''一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''


def drop(n):
    m=100
    k=1
    while  k <=n:
        m/=2
        k += 1
    print(m)

drop(10)