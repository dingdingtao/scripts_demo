'''
Author: dingdingtao
Date: 2020-12-04 14:57:15
LastEditTime: 2021-01-07 09:29:08
LastEditors: dingdingtao
Description: 获取数据存入mysql
'''
import pandas as pd
import datetime
import pymysql
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.types import TEXT
from sqlalchemy.types import BIGINT
from step_1_data import hive_presto
import argparse
import json
from step_1_data import cleaning_data
from tqdm import tqdm


CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh


'''
description: 读取sql语句
param {*} c 配置信息
return {*} sql语句
'''
def fetch_sql(c):
    sql_path = ""
    if c['sql_path'] != '':
        sql_path = c['sql_path'] + '\\'
    sql_path = sql_path + c['sql_filename']
    sqlfile = open(CURRENT_PATH+'\\..\\sql\\' + sql_path, 'r', encoding = 'utf8')
    sqltxt = sqlfile.readlines()
    sqlfile.close()
    sql = "".join(sqltxt)
    return sql


'''
description: 查询表中记录条数
param {*}
return {*} 如果表不存在或者没有记录返回1，如果有记录返回记录数+1
'''
def fetch_data_count():
    count = 1
    try:
        connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
        cursor = connection.cursor()
        sql = """select * from {table}""".format(table=config['table_name'])
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        count = len(result) + 1
    except Exception as e:
        pass
    return count


'''
description: 根据sql语句查询出敏感词到数据库
param {*}
return {*}
'''
def save_data(table, config):
    sqltxt = fetch_sql(config)
    print("查询数据.")
    data = hive_presto.sg_presto_hive(sqltxt)
    if None == data or 0 == len(data):
        print("无数据.")
        return False
    print("查询完成.")

    engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset={encoding}".format(user=dh.USER,passwd=dh.PASS,host=dh.HOST,port=dh.PORT,db=dh.DB,encoding=dh.CODE)) #root 用户：密码，@IP:host//库名=编码
    con = engine.connect()

    datas = []
    dtype = {}
    distinct = fetch_data_count()
    print("下载数据.")
    try:
        with tqdm(data, desc="download progress", ncols=80) as t:
            for d in t:
                tmp = d[0]
                for index,head in enumerate(table['tabledtype'].keys()):
                    if head == 'id':
                        d.insert(index,distinct)
                        dtype[head] = BIGINT
                        continue
                    if head == 'cid':
                        d.insert(index,config['cid'])
                        dtype[head] = BIGINT
                        continue
                    elif head == 'word':
                        d[index] = cleaning_data.regular_filtering(tmp)
                    else:
                        d.insert(index,"")
                    dtype[head] = TEXT
                distinct = distinct + 1
                datas.append(d)
    except Exception as e:
        t.close()
        print(e)
        return False
    t.close()

    df = pd.DataFrame(datas,columns=table['tabledtype'].keys())
    df.to_sql(name=config['table_name'], con=engine, if_exists='replace', index=False ,dtype=dtype) # if_exists='append'
    print("下载完成.")
    return True


'''
description: 
param {*} table
param {*} config
return {*}
'''
def run(table, config):
    try:
        has_data = save_data(table, config)
        return has_data
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    # run("")
    pass