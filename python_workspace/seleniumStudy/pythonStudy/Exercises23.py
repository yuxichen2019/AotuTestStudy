# -*- coding: utf-8 -*- 
# 2020/06/05 14:15 
# seleniumStudy
# Exercises23.py 
# company

'''打印出如下图案：
   *
  ***
 *****
*******
 *****
  ***
   *

'''


for i in range(1,5):
        for j in range(1,8):
            if j not in range(5-i,4+i):
                if j != 7:
                    print(' ',end='')
                else:
                    print(' ')
            else:
                if j == 7:
                    print('*')
                else:
                    print("*",end='')


for i in range(1,4):
    for j in range(1,8,):
        if j not in range(i+1,8-i):
            if j !=7:
                print(' ',end='')
            else:
                print(' ')
        else:
            if j==7:
                print('*')
            else:
                print('*',end='')