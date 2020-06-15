import csv
import os

from framework.UtilsRandom import UtilsRandom


class UtilsFile(object):
    def __init__(self, filePath):
        self.filePath = filePath

    # 写文件
    def write(self, fileData):
        csvFile = open(self.filePath, 'a', encoding='utf8', newline='')
        writer = csv.writer(csvFile)
        writer.writerows(fileData)
        csvFile.close()

    # 读取文件
    def read(self):
        csvFile = open(self.filePath, encoding='utf8')
        try:
            return csvFile.readlines()
        finally:
            csvFile.close()

    # 数据驱动读取CSV的数据
    def get_csv_data(filePath):
        if "testCase" in os.getcwd():
            dataPath = '../../data/'
        else:
            dataPath = './data/'
        value_rows = []
        with open(dataPath+filePath,encoding='utf8') as f:
            # 忽略表头
            f_csv = csv.reader(f)
            next(f_csv)
            for r in f_csv:
                value_rows.append(r)
        return value_rows


if __name__ == '__main__':
    utilsFile = UtilsFile("../data/data.csv")
    fileData = []
    for i in range(100):
        fileData.append([UtilsRandom.getChineseName(), UtilsRandom.getEmail(),UtilsRandom.getMobilePhone()])
        fileData.append(["姓名","邮箱","手机号码"])
        utilsFile.write(fileData)
    for line in utilsFile.read():
        print(line)