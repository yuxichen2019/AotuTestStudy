# -*- coding: utf-8 -*-
# 2020/6/7 16:24 
# interfaceTraining
# StudentManagement.py 
# company
import json
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from framework.UtilsDB import UtilsDB
from framework.UtilsRandom import UtilsRandom
from testCase.student.BaseCase import BaseCase


class TestStudentManagement(BaseCase):

    studentName = UtilsRandom.getChineseName()
    idcard = UtilsRandom.getIdcard()


    def add_student(self):

        url = self.baseURL  +  '/student/insert'
        data={
            "gradeId": "大一",
            "studentName": self.studentName,
            "sex": "女",
            "idCard":self.idcard,
            "classId": "3班"
        }

        header = {"Content-Type": "application/json","charset": "utf-8"}
        response = self.requests.sendRequests(url, data=json.dumps(data), headers=header)
        self.assertEqual(response.status_code, 200)
        print(self.studentName + '  '+ self.idcard)


    def getstudentIdbyname(self):
        self.name=self.studentName
        url1=self.baseURL + '/student/find/name/' + self.name
        response1=self.requests.sendRequests(url1,method='get')
        result=self.requests.getJsonFilesValue(response1,'data')
        stuId=result[0]['studentId']
        return stuId


    def add_student_score(self):
        url = self.baseURL + '/score/insert'
        data={
                "examId": "",
                "examInformation": "月考",
                "gradeId": "大三",
                "classId": "3班",
                "studentName": self.studentName,
                "studentId": self.getstudentIdbyname(),
                "chineseScore": "90",
                "mathScore": "91",
                "englishScore": "92",
                "compositeScore": "99",
                "totalScore": ""
            }

        header = {"Content-Type": "application/json", "charset": "utf-8"}
        response = self.requests.sendRequests(url, data=json.dumps(data), headers=header)
        self.assertEqual(response.status_code, 200)


    def get_all_score(self):
        #通过学号查询成绩
        dict={}
        url = self.baseURL + '/score/get/student/' + str(self.getstudentIdbyname())
        header = {"Content-Type": "application/json", "charset": "utf-8"}
        response = self.requests.sendRequests(url, method='get', headers=header)
        result=self.requests.getJsonFilesValue(response,'data')
        dict['姓名：'] = self.studentName
        dict['语文：'] = result[0]['chineseScore']
        dict['数学：'] = result[0]['mathScore']
        dict['英语：'] = result[0]['englishScore']
        print(dict)
        self.assertEqual(response.status_code, 200)


    def clear_table(self):
        # db = UtilsDB("localhost", "test", "root", "123456")
        db=UtilsDB(url='localhost', dbName='test', userName='root', passWord='123456')
        sql1='delete from score;'
        sql2='delete from student;'
        db.editData(sql1)
        db.editData(sql2)

    def teststuentflow(self):
        self.add_student()
        self.add_student_score()
        self.get_all_score()
        self.clear_table()


if __name__ == '__main__':
    report_path = os.path.dirname(__file__) + '/report/' + 'TestStudentManagement.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudentManagement)
    runner=HTMLTestRunner()
