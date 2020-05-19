import traceback
import os
import pymysql


class UtilsDB(object):
    def __init__(self, url, dbName, userName, passWord):
        self.url = url
        self.dbName = dbName
        self.userName = userName
        self.passWord = passWord

    """
        get connection to data base
    """

    def getConnection(self):
        return pymysql.connect(host=self.url,
                               port=3306,
                               user=self.userName,
                               passwd=self.passWord,
                               db=self.dbName,
                               charset='utf8')

    """
        execute sql for select 查询
    """

    def executeSql(self, sqlStr):
        connection = self.getConnection()
        try:
            cursor = connection.cursor()
            cursor.execute(sqlStr)
            dataAll = cursor.fetchall()
            for data in dataAll:
                print("Database data :", data)
            return dataAll
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
            connection.rollback()
        finally:
            connection.close()

    """
        execute sql for delete and update  改 删
    """

    def editData(self, sqlStr):
        connection = self.getConnection()
        try:
            cursor = connection.cursor()
            cursor.execute(sqlStr)
            connection.commit()
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
            connection.rollback()   #查询不需要回滚，其他操作如果异常  需要回滚
        finally:
            connection.close()

    """
       Execute sql file
       到处sql文件
    """
    def executeSqlFile(self, sqlFile):
        sqlCommand = 'mysql -h' + self.url + ' -u ' + self.userName + ' -p' + self.passWord + '< ' + sqlFile + ' --default-character-set=utf8'
        print('sql command is:', sqlCommand)
        result = os.popen(sqlCommand)
        print(result.readlines())


if __name__ == '__main__':
    utilsDB = UtilsDB("localhost", "studentinfo", "root", "123456")
    #utilsDB.executeSql('select st1.name,s1.chinese from class c1,score s1, student st1 where c1.id=st1.class_id and st1.id =s1.student_id and s1.chinese>80 and c1.name LIKE "%一年级%"')
    #utilsDB.editData("insert into student VALUES(4,1,'小李',16)")
    #utilsDB.editData("insert into student VALUES(4,1,'小李',16)")
    #utilsDB.editData("DELETE from student where id = 4")

    # 新增100行数据
    # for i in range(100):
    #     sqlStr = "insert into testdata (input,expect) VALUES('张三" + str(i) + "','羽毛球" + str(i) + "')"
    #     print(sqlStr)
    #     utilsDB.editData(sqlStr)
    # # 修改前50行数据
    # sqlStr = "update testdata SET input='妞妞' where id BETWEEN 313 AND 363"
    # print(sqlStr)
    # utilsDB.editData(sqlStr)
    # # # 删除最后50行
    # sqlStr = "delete from testdata where id BETWEEN 364 AND 414"
    # print(sqlStr)
    # utilsDB.editData(sqlStr)
    # # 最后执行查询
    # utilsDB.executeSql("select input,expect from testData")
