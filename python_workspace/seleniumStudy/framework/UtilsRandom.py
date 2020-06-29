import random

from framework.UtilsDate import UtilsDate


class UtilsRandom:
    # 随机生成中文姓名
    @staticmethod
    def getChineseName():
        first_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                       '许',
                       '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                       '庞',
                       '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        last_names = random.randint(0x4e00, 0x9fbf)
        return random.choice(first_names) + chr(last_names)+str(UtilsDate.getTimeStamp())

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


if __name__ == '__main__':
    print("随机获取的中文名：" + UtilsRandom.getChineseName())
    print("随机生成的手机号码：" + UtilsRandom.getMobilePhone())
    print("随机生成的邮箱：" + UtilsRandom.getEmail())
