# -*- coding: utf-8 -*- 
# 2020/06/29 17:37 
# seleniumStudy
# Exercises29.py 
# company


'''给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。'''

s = int(input('请输入一个不多于5位的正整数：'))
a = int(s/10000)
b = int(s/1000%10)
c = int(s/100%10)
d = int(s/10%10)
e = s%10

if a == 0:
    if b == 0:
        if c == 0:
            if d == 0:
                if e==0:
                    print('请输入合法数字')
                else:
                    print('1位数: %d' % e)
            else:print('2位数{0}{1}'.format(e,d))
        else:print('3位数{0}{1}{2}'.format(e,d,c))
    else:print('4位数{0}{1}{2}{3}'.format(e,d,c,b))
else:print('5位数 {0}{1}{2}{3}{4}'.format(e,d,c,b,a))

