# -*- coding: utf-8 -*- 
# 2020/05/25 17:38 
# seleniumStudy
# Exercises14.py 
# company

'''
将一个正整数分解质因数。例如：输入90，打印出90=2 * 3 * 3 * 5
'''

# def reduceNum(n):
#    print ('{} = '.format(n),end='')
#    if not isinstance(n, int) or n <= 0 :
#        print ('请输入一个正确的数字!')
#        exit(0)
#    elif n in [1] :
#        print ('{}'.format(n))
#    while n not in [1] : # 循环保证递归
#        for index in range(2, int(n) + 1):
#            if n % index == 0:
#                n /= index # n 等于 n/index
#                if n == 1:
#                    print (index,end='')
#                else : # index 一定是素数
#                    print ('{} *'.format(index),end='')
#                break
# reduceNum(2)


n = int(input('请输入一个正整数：'))
print('{} = '.format(n),end='')
if not isinstance(n,int) or n<=0:
    print('请输入正确的正整数！！！')
else:
    while n != 1:
        #print('{}'.format(n))
        for i in range(2,int(n)+1):
            if n % i == 0:
                n /= i
                if n==1:
                    print(i,end='')
                else:
                    print('{} * '.format(i),end='')
                break

