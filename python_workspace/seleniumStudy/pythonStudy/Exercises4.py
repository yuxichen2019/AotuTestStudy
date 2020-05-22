# -*- coding: utf-8 -*- 
# 2020/05/21 17:22 
# seleniumStudy
# fourth_question.py 
# company

'''
题目:输入某年某月某日,判断这一天是这一年的第几天?
1.程序分析:以3月5日为例,应该先把前两个月的加起来,然后再加上5天即本年的第几天,
特殊情况況,闰年且输入月份大于3时需考虑多加一天。
'''

date = input('请输入年月日')
list1=date.split('-')
year = int(list1[0])
month = int(list1[1])
day = int(list1[2])


# if year%4 == 0 :
#     if year%100 == 0:
#         if year%400 ==0:
#             y = 1
#         else:
#             y = 0
#     else:
#         y = 1
# else:
#     y = 0

if (year%4==0) or (year%400==0) and (year%100!=0):
    y=1

else:
    y=0

list=[31,28,31,30,31,30,31,31,30,31,30,31]
num=0

while date:
    if y == 0:
        if month == 1:
            num = day
            print( date +'A是这一年的第' + str(num) + '天')
            break
        else:
            for i in range(month-1):
                num +=list[i]
            num += day - list[month-1]
            print(date +'B是这一年的第' + str(num) + '天')
            break
    if y == 1:
        if month == 1:
            num = day
            print(date +'C是这一年的第' + str(num) + '天')
            break
        else:
            for i in range(month-1):
                num = num + list[i]
            num = num + day
            print(date +'D是这一年的第' + str(num) + '天')
            break