'''
Author: dingdingtao
Date: 2020-12-06 15:06:25
LastEditTime: 2021-01-06 15:31:15
Description: pymysql
'''
import pymysql



"""
pymysql参考
https://www.runoob.com/python3/python3-mysql.html
"""



username = "root"
password = "root"
host = "127.0.0.1"
port = 3306
db = "db_name"
charset = "utf8"



'''
Description: 常规查询
param {*}
return {*}
'''
def mysql():
    """ 
    连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user=username, password=password, db='t1', charset='utf8')
    host - 主机地址
    port - 端口
    user - 用户名
    password - 密码
    db - 数据库名
    charset - 编码
    """
    conn = pymysql.connect(host=host, port=port, user=username, password=password, db=db, charset=charset)
    print(conn)


    """
    创建游标,操作数据库用
    """
    cursor = conn.cursor()


    """
    sql语句
    """
    sql = "select * from t1.userinfo where username='%s' and pwd='%s'" %(username, password)


    """
    执行语句,返回结果或影响的记录条数
    """
    result = cursor.execute(sql)

    '''
    多条执行
    cursor.executemany(sql_sav, data)
    '''

    print(result)


    '''如果执行select语句以外的语句需要提交执行结果'''
    # conn.commit()

    """
    关闭连接，游标和连接都要关闭
    """
    cursor.close()
    conn.close()

