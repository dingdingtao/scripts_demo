'''
Author: dingdingtao
Date: 2020-12-30 14:23:15
LastEditTime: 2021-03-03 10:30:28
LastEditors: dingdingtao
Description: 从hive查数据插入mysql
'''
import time
import pymysql
from bin import hive_presto
from bin import fetch_config
from bin import fetch_sql


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
description: 插入数据
param {*} c 配置config.json
param {*} d 要插入的数据
return {*}
'''
def insert_into(connection, cursor, c, d):
    data = []
    for dt in d:
        data.append(connection.escape(dt))
    sql = """insert into {table}({fileds}) values({values})""".format(table=c['mysql_table'], fileds=",".join(c['mysql_tablehead']), values=",".join(data))
    cursor.execute(sql)
    connection.commit()


'''
description: 从hive查数据转存到mysql
param {*}
return {*}
'''
def run():
    '''读配置文件 config.json, _config.json'''
    config, _config = fetch_config.fetch()

    '''读sql语句'''
    sql = fetch_sql.fetch(config)

    print(sql)

    '''sg Hive'''
    datas = hive_presto.hive_presto_sg_sql(sql)
    
    '''hk Hive'''
    # datas = hive_presto.hive_presto_hk_sql(sql)
    
    '''hive'''
    # datas = hive_presto.hive_presto_sql(sql)
    connection, cursor = connect_mysql(_config)
    for current,data in enumerate(datas):
        print(data,"{current}/{total}".format(current=(current + 1),total=len(datas)))
        insert_into(connection, cursor, config, data)
        time.sleep(0.1)
    close_connect(connection, cursor)
    print("done.")


if __name__ == "__main__":
    run()