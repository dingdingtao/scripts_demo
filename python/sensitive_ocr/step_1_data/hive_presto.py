'''
Author: dingdingtao
Date: 2020-12-04 14:55:31
LastEditTime: 2021-03-12 19:01:21
LastEditors: dingdingtao
Description: hive查询
'''
import prestodb
import datetime

'''
description: hive_presto新加坡集群查询
param {*} sql_text
return {*} 查询结果
'''
def sg_presto_hive(sql_text):
    applicationName = "applicationName" 
    props = {"enable_hive_syntax": "true"}
    conn = prestodb.dbapi.connect(
        host='host',
        port=0000,
        user='username',
        catalog='hive',
        schema='default',
        source=applicationName,
        session_properties=props
        )
    cur = conn.cursor()
    data = cur.execute(sql_text)
    try:
        data = cur.fetchall()
    except prestodb.exceptions.PrestoUserError:
        print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S") + '--sql error')

    return data


'''
description: hive_presto香港集群查询
param {*} sql
return {*} 查询结果 类型：list
'''
def hk_presto_hivesql(sql):
    applicationName = "applicationName"
    props = {"enable_hive_syntax": "true"}
    conn = prestodb.dbapi.connect(
        host='host',
        port=0000,
        user='username',
        catalog='hive',
        schema='default',
        source=applicationName,
        session_properties=props
        )
    cur = conn.cursor()
    data = cur.execute(sql)
    try:
        data = cur.fetchall()
    except prestodb.exceptions.PrestoUserError:
        print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S") + '--sql error')

    return data



'''
description: hive_presto查询
param {*} sql
return {*} 查询结果 类型：list
'''
def get_presto_hivesql(sql):
    applicationName = "applicationName"
    props = {"enable_hive_syntax": "true"}
    conn = prestodb.dbapi.connect(
        host='host',
        port=0000,
        user='username',
        catalog='hive',
        schema='default',
        source=applicationName,
        session_properties=props
        )
    cur = conn.cursor()
    data = cur.execute(sql)
    try:
        data = cur.fetchall()
    except prestodb.exceptions.PrestoUserError:
        print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S") + '--sql error')

    try:
        if len(data) == 0:
            data = sg_presto_hive(sql)
    except:
        data = sg_presto_hive(sql)

    return data

