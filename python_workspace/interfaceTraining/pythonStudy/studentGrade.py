class StudentGrade:
    name = ''
    score = 0
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def gradeRank(self, studentsList):
        length = len(studentsList)
        for i in range(0, length - 1):
            for j in range(0, length - 1 - i):
                if studentsList[j].score < studentsList[j + 1].score:
                    tmp = studentsList[j]
                    studentsList[j] = studentsList[j + 1]
                    studentsList[j + 1] = tmp
        for item in studentsList:
            print(item.name
                  + ":" + str(item.score))
    # 构造方法



if __name__ == '__main__':
    ligang1 = StudentGrade('李刚1', 150)
    ligang2 = StudentGrade('李刚2', 80)
    ligang3 = StudentGrade('李刚3', 160)
    ligang4 = StudentGrade('李刚4', 90)
    ligang = [ligang1, ligang2, ligang3, ligang4]
    ligang4.gradeRank(ligang)
