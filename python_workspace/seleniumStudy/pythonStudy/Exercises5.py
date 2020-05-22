# -*- coding: utf-8 -*- 
# 2020/05/22 15:27 
# seleniumStudy
# Exercises5.py 
# company

'''
输入三个整数，然后有小到大进行排序
'''

a=input('请输入第一个整数')
b=input('请输入第二个整数')
c=input('请输入第三个整数')

list=[a,b,c]
# list1=[]
# for i in list:
#     for j in list:
#         for k in list:
#             if i<j and j<k:
#                 list1.append(str(i))
#                 list1.append(str(j))
#                 list1.append(str(k))
#                 print(list1)
list.sort()
print(list)

