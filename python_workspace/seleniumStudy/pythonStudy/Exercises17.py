# -*- coding: utf-8 -*- 
# 2020/05/26 11:37 
# seleniumStudy
# Exercises16.py 
# company


'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''

str='a 1P1 d22 L3$ 1@^&0*A %^ &*d hs2  a20+k j'
others=0
nums=0
letter=0
space=0

str1=list(str)

for i in str1:
    if i.isdigit():
        nums+=1
    elif i.isspace():
        space+=1
    elif i.isalpha():
        letter+=1
    else:
        others+=1

print('数字：{}个，字母：{}个，空格：{}个，其他：{}个'.format(nums,letter,space,others))
