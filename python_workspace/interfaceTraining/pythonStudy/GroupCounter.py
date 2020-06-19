class GroupCounter:

    def readFile(self, filePath):
        dataArray = []
        for line in open(filePath):
            dataArray.append(line)
        print("初始数据", dataArray)
        return dataArray

    def splitStr(self, dataArray):
        for item in dataArray:
            if "/" in item:
                for ele in item.split("/"):
                    dataArray.append(ele)
        # print("拆分之后的数据", dataArray)
        # 重复元素的数组下标
        deleteItemIndexs = []
        # 新的数据数组
        newDataArray = []
        length = len(dataArray)
        for i in range(0, length):
            if "/" in dataArray[i]:
                deleteItemIndexs.append(i)
            if i not in deleteItemIndexs:
                if "\n" in dataArray[i]:
                    newElement = dataArray[i].replace("\n", "")
                    newDataArray.append(newElement)
                else:
                    newDataArray.append(dataArray[i])
        print("去换行拆分之后的数据", newDataArray)
        return newDataArray

    def groupCounter(self, dataArray):
        dict = {}
        for key in dataArray:
            dict[key] = dict.get(key, 0) + 1
        print("统计结果", dict)


if __name__ == '__main__':
    groupCounter = GroupCounter()
    dataArray = groupCounter.readFile("../data/characters.txt")
    dataArray1 = groupCounter.splitStr(dataArray)
    groupCounter.groupCounter(dataArray1)
