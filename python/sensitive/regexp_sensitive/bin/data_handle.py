'''
Author: dingdingtao
Date: 2020-12-30 10:55:04
LastEditTime: 2021-01-07 10:31:53
LastEditors: dingdingtao
Description: 数据处理
'''
import pymysql
import os
import sys
import pandas as pd


CURRENT_PATH = os.path.dirname(__file__)


'''
description: 读数据excel文件
param {*} c 配置信息
return {*} 所有数据
'''
def fetchall_data_sensitive(c):
    alldata = pd.read_excel(os.path.join(CURRENT_PATH, ".." + os.path.sep + "data" + os.path.sep + c['filename']), sheet_name=c['sheetname'], header=None)
    data_list = alldata.values.tolist()
    data = []
    for d in data_list:
        data.append(d)
    return data


'''
description: 从mysql读数据
param {*} c 配置信息
return {*} 所有记录
'''
def fetch_data(c):
    sql = """
        select id,word from regexp_sensitive_word_datas 
    """
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    cursor.execute(sql)
    r = cursor.fetchall()
    cursor.close()
    connection.close()
    return r


'''
description: 查询数据转存到mysql
param {*} c 配置信息
return {*} 所有记录
'''
def fetch_data_mysql(c):
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    datas = fetchall_data_sensitive(c)
    for i,data in enumerate(datas):
        sql = "insert into regexp_sensitive_word_datas(id,word) values({id},{word})".format(id=i,word=connection.escape(data[0]))
        cursor.execute(sql)
        connection.commit()
    cursor.close()
    connection.close()
    data = fetch_data(c)
    return data



'''
description: 读正则excel文件
param {*} c 配置信息
return {*} 所有正则
'''
def fetchall_regexp_sensitive(c):
    alldata = pd.read_excel(os.path.join(CURRENT_PATH, ".." + os.path.sep + "regexp" + os.path.sep + c['reg_filename']), sheet_name=c['reg_sheetname'], header=None)
    data_list = alldata.values.tolist()
    data = []
    print(data_list)
    for d in data_list:
        data.append(d)
    return data


'''
description: 从mysql读取正则表
param {*} c 配置信息
return {*} 所有正则
'''
def fetch_regexp(c):
    sql = """
        select id,reg from regexp_sensitive_word_regs 
    """
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    cursor.execute(sql)
    r = cursor.fetchall()
    cursor.close()
    connection.close()
    return r



'''
description: 读正则转存到mysql
param {*} c 配置信息
return {*} 所有正则记录
'''
def fetch_regexp_mysql(c):
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    datas = fetchall_regexp_sensitive(c)
    for i,data in enumerate(datas):
        sql = "insert into regexp_sensitive_word_regs(id,reg) values({id},{reg})".format(id=i,reg=connection.escape(data[0]))
        cursor.execute(sql)
        connection.commit()
    cursor.close()
    connection.close()
    data = fetch_regexp(c)
    return data


'''
description: 保存结果
param {*} c 配置信息
param {*} datas 数据列表
return {*}
'''
def save_result(c, datas):
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    for i,data in enumerate(datas):
        wid = connection.escape(data[0])
        rid = connection.escape(data[1])
        word = connection.escape(data[2])
        reg = connection.escape(data[3])
        hit = connection.escape(data[4])
        sql = "insert into regexp_sensitive_word_results(wid,rid,word,reg,hit) values({wid},{rid},{word},{reg},{hit})".format(wid=wid,rid=rid,word=word,reg=reg,hit=hit)
        cursor.execute(sql)
        connection.commit()
    cursor.close()
    connection.close()


'''
description: 从mysql读取所有结果
param {*} c 配置信息
return {*} 匹配结果
'''
def fetch_result(c):
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    sql = "select wid,rid,word,reg,hit from regexp_sensitive_word_results"
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    connection.close()
    return datas


'''
description: 导出结果数据到excel
param {*} c 配置信息
param {*} d 数据列表
return {*} 导出文件的路径
'''
def export_datas(c, d):
    save_result(c, d)
    datas = fetch_result(c)
    df = pd.DataFrame(datas)
    export_path = os.path.join(os.path.join(CURRENT_PATH, ".." + os.path.sep + "result"), "result - " + str(c['filename']))
    df.to_excel(export_path, "Sheet1")
    return export_path


'''
description: 清空数据表
param {*} c 配置信息
return {*}
'''
def clear_table(c):
    connection = pymysql.connect(host=c['host'], port=c['port'], user=c['user'],password=c['password'], db=c['db'], charset=c['charset'])
    cursor = connection.cursor()
    sql1 = """delete from regexp_sensitive_word_results"""
    sql2 = """delete from regexp_sensitive_word_regs"""
    sql3 = """delete from regexp_sensitive_word_datas"""
    cursor.execute(sql1)
    connection.commit()
    cursor.execute(sql2)
    connection.commit()
    cursor.execute(sql3)
    connection.commit()
    cursor.close()
    connection.close()