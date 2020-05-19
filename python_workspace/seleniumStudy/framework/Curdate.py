# -*- coding: utf-8 -*- 
# 2020/4/19 11:25 
# seleniumStudy
# Curdate.py 
# company

import datetime

class Curdate:
    def get_curtime(self):
        curr_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        print(curr_time)

if __name__ == '__main__':
    ct=Curdate()
    ct.get_curtime()