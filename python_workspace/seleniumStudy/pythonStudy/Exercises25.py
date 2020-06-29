# -*- coding: utf-8 -*- 
# 2020/06/29 16:36 
# seleniumStudy
# Exercises25.py 
# company

'''求1+2!+3!+...+20!的和。'''

# s2=1
# for i in range(1,21):
#     s1=1
#     for j in range(1,i+1):
#         s1*=j
#     print(s1)
#     s2+=s1
#
# print(s2)


l=range(1,21)

def op(x):
    t=1
    for i in range(1,x+1):
        t*=i
    return t

s=sum(map(op,l))

print(s)