# -*- coding: utf-8 -*- 
# 2020/05/21 12:18 
# seleniumStudy
# the_third_question.py 
# company

'''
一个整数,它加上100后是一个完全平方数,再加上268又是一个完全平方数,请问该数是多少?
程序分析:在10万以内判断,先将该数加上100后再开方,再将该数加上268后再开方,如果开方后的结果满足如下条件,即是结果。
'''



for i in range(100000):
    if (i+100) ** 0.5 == int((i+100) ** 0.5):
        if (i+368) ** 0.5==int((i+368) ** 0.5):
            print(i)
            
#注意：100 ** 0.5 =10.0  isinstance也返回false了.
# isinstance(a,int) 判断a是不是int，是的返回True。



