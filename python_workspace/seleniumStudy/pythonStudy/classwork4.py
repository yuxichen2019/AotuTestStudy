# -*- coding: utf-8 -*- 
# 2020/5/10 16:01 
# seleniumStudy
# 4.py 
# company



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
