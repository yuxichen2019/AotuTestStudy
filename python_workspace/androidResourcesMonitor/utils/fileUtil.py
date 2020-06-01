import csv


class FileUtil(object):
    def __init__(self, filePath,alldata):
        self.filePath = filePath
        self.alldata = alldata

    # def __init__(self, filePath):
    #     self.filePath = filePath

    # 写CSV文件
    def saveDataToCSV(self):
        csvfile = open(self.filePath, 'a',encoding='utf8',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    # 写TXT文件
    def saveDataToTXT(self):
        txtfile = open(self.filePath, 'a',encoding='utf8',newline='')
        txtfile.write(self.alldata+"\n")
        txtfile.close()
    # 读取TXT文件
    def readDataFromTXT(self):
        txtFile = open(self.filePath)
        try:
            return txtFile.readlines()
        finally:
            txtFile.close()