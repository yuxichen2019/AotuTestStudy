import random
import time


class UtilsRandom(object):
    # 随机生成中文姓名
    @staticmethod
    def getChineseName():
        first_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                       '许',
                       '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                       '庞',
                       '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        last_names = random.randint(0x4e00, 0x9fbf)
        return random.choice(first_names) + chr(last_names)

    # 随机生成手机号码
    @staticmethod
    def getMobilePhone():
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成邮箱
    @staticmethod
    def getEmail():
        emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
        randomEmail = random.choice(emailtype)
        rang = random.randint(4, 10)
        number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        randomNumber = "".join(random.choice(number) for i in range(rang))
        email = randomNumber + randomEmail
        return email

    # 随机数字
    @staticmethod
    def getNo(count):
        return "".join(random.choice("0123456789") for i in range(count))

    #随机生成身份证号码
    @staticmethod
    def getIdcard():
        #前六位
        first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428',
                      '362429', '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105',
                      '110106', '110107', '110108', '110109', '110111']
        first = random.choice(first_list)

        '''生成年份'''
        now = time.strftime('%Y')
        #1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(1948,int(now)-18)
        age = int(now) - second


        '''生成月份'''
        three = random.randint(1,12)
        #月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)

        '''生成日期'''
        four = random.randint(1,31)
        #日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)

        '''生成身份证后四位'''
        #后面序号低于相应位数，前面加上0填充
        five = random.randint(1,9999)
        if five < 10:
            five = '000' + str(five)

        elif 10 < five < 100:
            five = '00' + str(five)

        elif 100 < five < 1000:
            five = '0' + str(five)

        IDcard = str(first)+str(second)+str(three)+str(four)+str(five)
        return IDcard

if __name__ == '__main__':
    print("随机获取的中文名：" + UtilsRandom.getChineseName())
    print("随机生成的手机号码：" + UtilsRandom.getMobilePhone())
    print("随机生成的邮箱：" + UtilsRandom.getEmail())
    print("随机生成的数字：" + UtilsRandom.getNo(3))
    print('随机生成的身份证号码：' + UtilsRandom.getIdcard())