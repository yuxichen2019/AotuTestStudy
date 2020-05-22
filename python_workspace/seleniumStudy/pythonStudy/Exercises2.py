# -*- coding: utf-8 -*- 
# 2020/05/14 11:15 
# seleniumStudy
# countBonus.py 
# company

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

'''


def getbonus(profit):
    bonus=0
    if profit <= 10:
        bonus = 0.1 * profit

    elif 10 < profit <= 20:
        bonus = 1  +  (profit-10) * 0.075
    elif 20 < profit <= 40:
        bonus = 1.75 + (profit-20) * 0.05
    elif 40 < profit <= 60:
        bonus = 2.75 + (profit-40) * 0.03
    elif 60 < profit <=100:
        bonus = 3.35 + (profit-60) * 0.015
    elif 100 < profit:
        bonus = 3.95 + (profit-100) * 0.01

    print('当利润为：%s 万时，奖金为: %s 元' % (profit,bonus*10000))


getbonus(5)
getbonus(10)
getbonus(20)
getbonus(40)
getbonus(60)
getbonus(80)
getbonus(200)