'''
Author: dingdingtao
Date: 2021-01-01 20:01:20
LastEditTime: 2021-01-05 18:35:30
Description: 从mysql查数据
'''
import pymysql
import time


'''
Description: 连接mysql
param {*} _c 数据库配置信息
return {*} connection 数据库连接, cursor 游标
'''
def connect_mysql(_c):
    connection = pymysql.connect(host=_c['host'], port=_c['port'], user=_c['user'],password=_c['password'], db=_c['db'], charset=_c['charset'])
    cursor = connection.cursor()
    return connection, cursor


'''
Description: 关闭连接
param {*} connection 数据库连接
param {*} cursor 游标
return {*}
'''
def close_connect(connection, cursor):
    cursor.close()
    connection.close()


'''
Description: sql查询,返回前count条
param {*} _config 数据库配置
param {*} sql sql语句
param {*} start 记录开始索引
param {*} count 记录条数
return {*} 查询结果，从start开始的count条记录
'''
def fetch_count(_config, sql, count=100, start=0):
    try:
        connection, cursor = connect_mysql(_config)
        cursor.execute(sql)
        datas = cursor.fetchall()
        close_connect(connection, cursor)
        if not isinstance(start, int) or start < 0 or start >= len(datas):
            return [], False
        if not isinstance(count, int) or count <= 0:
            return [], False
        return datas[start:count + 1], True
    except Exception as e:
        print(e)
        return [], False


'''
Description: sql查询,返回所有结果
param {*} _config 数据库配置
param {*} sql sql语句
return {*} 查询结果
'''
def fetch_all(_config, sql):
    try:
        connection, cursor = connect_mysql(_config)
        cursor.execute(sql)
        datas = cursor.fetchall()
        close_connect(connection, cursor)
        return datas, True
    except Exception as e:
        print(e)
        return [], False