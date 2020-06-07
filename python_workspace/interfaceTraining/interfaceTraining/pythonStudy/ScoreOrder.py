class Student:
    name = ''
    score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def descSort(self, studentsList):
        length = len(studentsList)
        for i in range(0, length - 1):
            for j in range(0, length - 1 - i):
                if studentsList[j].score < studentsList[j + 1].score:
                    tmp = studentsList[j]
                    studentsList[j] = studentsList[j + 1]
                    studentsList[j + 1] = tmp
        for item in studentsList:
            print(item.name+":"+str(item.score))


if __name__ == '__main__':
    ligang1 = Student("李刚1", 150)
    ligang2 = Student("李刚2", 80)
    ligang3 = Student("李刚3", 160)
    ligang4 = Student("李刚4", 90)
    studentsList = [ligang1, ligang2, ligang3, ligang4]
    # 倒序排列
    ligang1.descSort(studentsList)
    # 成绩求和
    length = len(studentsList)
    scoreSum=0
    for i in range(0, length):
        scoreSum=scoreSum+studentsList[i].score
    print("成绩总和是：",scoreSum)

