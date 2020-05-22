# -*- coding: utf-8 -*- 
# 2020/5/10 16:01 
# seleniumStudy
# 4.py 
# company

'''
题目:有1、2、3、4个数字,能组成多少个互不相同且无重复数字的三位数?都是多少?
1.程序分析:可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
'''

list=['1','2','3','4']
list1=[]
for i in list:
    for j in list:
        for x in list:
            if x!=i and x!=j and i!=j:
                a=i + j + x
                list1.append(a)

print(list1)
print(len(list1))
