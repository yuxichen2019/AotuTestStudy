# -*- coding: utf-8 -*- 
# 2020/05/26 17:57 
# seleniumStudy
# Exercises19.py 
# company


'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''


from sys import stdout
for j in range(2, 1001):
    k = []
    n = 0
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)

    if s == 0:
        print(j)

        for i in range(n-1):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n-1])


'''
#自己的
for i in range(2,1001):
    list=[]
    a=0
    for j in range(1,int(i)):
        if i%j== 0:
            a+=j
            list.append(j)
    if i == a:
        print('{} '.format(i))
        for k in list:
            if k != list[-1]:
                print(k,end=' ')
            else:
                print(k)
'''