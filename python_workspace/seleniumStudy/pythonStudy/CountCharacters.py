# -*- coding: utf-8 -*- 
# 2020/05/13 16:21 
# seleniumStudy
# Statistics_times.py 
# company


file_path=r'E:\yuxichen\Study\python_workspace\seleniumStudy\data\ts.txt'

def getword(filepath):
    f=open(filepath)
    list_line=[]
    while f:
        d=f.readline()
        list_line.extend(d.split())
        if not d:
            break
    list_word=[]
    for i in list_line:
        list_word.extend(i.split('/'))
    # print(list_line)
    # print(list_word)
    return list_word

def get_count(list):
    dict={}
    for i in list:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    print(dict)



get_count(getword(file_path))

