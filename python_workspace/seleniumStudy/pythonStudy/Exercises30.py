# -*- coding: utf-8 -*- 
# 2020/06/29 17:37 
# seleniumStudy
# Exercises30.py 
# company

'''一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''


s=int(input('请输入一个五位数：'))

a = int(s/10000)
b = int(s/1000%10)
c = int(s/100%10)
d = int(s/10%10)
e = s%10

if a == e:
    if b == d:
        print('回文数')
    else:
        print('不是回文数')
else:print('不是回文数')