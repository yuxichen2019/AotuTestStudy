# -*- coding: utf-8 -*- 
# 2020/05/26 12:19 
# seleniumStudy
# Exercises18.py 
# company


'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

a=int(input('a='))
n=int(input('n='))

sn=0
list=[]
for i in range(n):
    sn+=a * (10 ** i)
    list.append(sn)
    print('{} + '.format(sn),end='')


sum=0
for j in list:
    sum+=j

print(sum)