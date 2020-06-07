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
        execute sql for select
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
        execute sql for delete and update
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
            connection.rollback()
        finally:
            connection.close()

    """
       Execute sql file
    """
    def executeSqlFile(self, sqlFile):
        sqlCommand = 'mysql -h' + self.url + ' -u ' + self.userName + ' -p' + self.passWord + '< ' + sqlFile + ' --default-character-set=utf8'
        print('sql command is:', sqlCommand)
        result = os.popen(sqlCommand)
        print(result.readlines())


if __name__ == '__main__':
    utilsDB = UtilsDB("localhost", "pymysql123", "root", "root")
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
    utilsDB.executeSqlFile("..\data\db.sql")
