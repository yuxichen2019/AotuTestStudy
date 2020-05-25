# -*- coding: utf-8 -*- 
# 2020/05/25 14:51 
# seleniumStudy
# Exercies8.py 
# company


'''
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''

for i in range(1,10):
    print('')
    for j in range(1,i+1):
        #print(str(j) +'*'+str(i) + '=' + str(i*j) ,end= '\t' )
        print("{0} * {1} = {2}".format(str(j),str(i),str(i*j)),end='\t')



