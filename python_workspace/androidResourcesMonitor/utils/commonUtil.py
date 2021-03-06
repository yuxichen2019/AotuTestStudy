import os
import traceback


class CommonUtil(object):
    def __init__(self, progressName,index):
        self.progressName = progressName
        self.index=index

    def getPid(self):
        result = os.popen("adb shell ps | findstr "+self.progressName)
        try:
            if result:
                pidStr = "#".join(result.readlines()[0].split())
                pid = pidStr.split("#")[self.index]
                print("pid is:" + pid)
                return pid
        except:
            traceback.print_exc()
            #Python使用traceback.print_exc()来代替print e 来输出详细的异常信息

# if __name__ == "__main__":
#     fileUtil = FileUtil("cpustatus.csv")
#     print(fileUtil.readFiles()[0:])
