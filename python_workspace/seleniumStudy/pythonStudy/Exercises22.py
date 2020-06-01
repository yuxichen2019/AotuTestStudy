# -*- coding: utf-8 -*- 
# 2020/06/01 17:22 
# seleniumStudy
# Exercises22.py 
# company


'''两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。'''


list1=['a','b','c']
list2=['x','y','z']
list=[]
list3=[]


for i in list1:
    for j in list2:
        list.append(i+j)


for k in list:
    if k not in ('ax','cx','cz'):



