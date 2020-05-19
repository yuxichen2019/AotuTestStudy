# -*- coding: utf-8 -*-
# 2020/5/16 14:53 
# seleniumStudy
# UtilsMysql.py 
# company
from time import sleep

import pymysql


class UtilsMysql:
    def __init__(self,ip,port,user,password,dbname):
        self.ip=ip
        self.port=port
        self.user=user
        self.password=password
        self.dbname=dbname

    def __getConnection(self):
        if not self.dbname:
            raise (NameError, "没有设置数据库信息")
        self.connect = pymysql.connect(host=self.ip,user=self.user,password=self.password,database=self.dbname,charset="utf8")
        cur = self.connect.cursor()
        print(cur)
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def excuteQueey(self,sql):

        cur = self.__getConnection()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.connect.close()
        print(resList)
        return resList

    def excuteOther(self):
        pass


u=UtilsMysql('localhost',3306,'root','Sy6660com@','studentinfo')
u.excuteQueey('SELECT name FROM student t1 left join score t2 on t1.id = t2.student_id where t2.chinese > 80')