# -*- coding: utf-8 -*- 
# 2020/6/7 16:24 
# interfaceTraining
# StudentManagement.py 
# company
import json

from framework import UtilsDB
from framework.UtilsRandom import UtilsRandom
from testCase.student.BaseCase import BaseCase


class TestStudentManagement(BaseCase):

    studentName = UtilsRandom.getChineseName()
    idcard = UtilsRandom.getIdcard()


    # def testadd_student(self):
    #
    #     url = self.baseURL  +  '/student/insert'
    #     data={
    #         "gradeId": "大一",
    #         "studentName": self.studentName,
    #         "sex": "女",
    #         "idCard":self.idcard,
    #         "classId": "3班"
    #     }
    #
    #     header = {"Content-Type": "application/json","charset": "utf-8"}
    #     response = self.requests.sendRequests(url, data=json.dumps(data), headers=header)
    #     self.assertEqual(response.status_code, 200)
    #     print(self.studentName + self.idcard)
    #
    #
    # def testadd_student_score(self):
    #     url = self.baseURL + '/score/insert'
    #     data={
    #             "examId": "",
    #             "examInformation": "月考",
    #             "gradeId": "大三",
    #             "classId": "3班",
    #             "studentName": self.studentName,
    #             "studentId": "005",
    #             "chineseScore": "90",
    #             "mathScore": "91",
    #             "englishScore": "92",
    #             "compositeScore": "99",
    #             "totalScore": ""
    #         }
    #
    #     header = {"Content-Type": "application/json", "charset": "utf-8"}
    #     response = self.requests.sendRequests(url, data=json.dumps(data), headers=header)
    #     self.assertEqual(response.status_code, 200)

    #
    # def testget_all_score(self):
    #     url = self.baseURL + '/score/get/all'
    #     header = {"Content-Type": "application/json", "charset": "utf-8"}
    #     response = self.requests.sendRequests(url, method='get', headers=header)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 200)


    def testclear_table(self):

        db=UtilsDB(url='localhost', dbName='test', userName='root', passWord='123456')
        sql1='delete form score'
        sql2='delete form student'
        db.editData(sql1)
        db.editData(sql2)


if __name__ == '__main__':
    a=TestStudentManagement()
    a.testclear_table()