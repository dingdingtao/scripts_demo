'''
Author: dingdingtao
Date: 2020-12-04 15:13:45
LastEditTime: 2021-03-12 17:48:08
LastEditors: dingdingtao
Description: 
'''
import pandas as pd
import pymysql
import json
import os
import sys
import re
import jpype
from sqlalchemy import create_engine
from sqlalchemy.types import TEXT
from sqlalchemy.types import BIGINT

'''
引入base_config
获取配置文件config.json的所有信息
'''
CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../config"))
import base_config

CONFIG, _CONFIG = base_config.get_all()

'''
HOST 数据库主机名
PORT 端口
USER 用户名
PASS 密码
DB 库名
CODE 编码
'''
HOST  = CONFIG['host']
PORT  = CONFIG['port']
USER  = CONFIG['user']
PASS  = CONFIG['pass']
DB    = CONFIG['db']
CODE  = CONFIG['charset']


'''

'''
OUT_TABLE = _CONFIG['outTable']
CONFIG_TABLE = _CONFIG['configTable']
RECORD_TABLE = _CONFIG['recordTable']
SENDMAIL_TABLE = _CONFIG['sendmailTable']

'''
TABLE 表名
SQL SQL语句
'''
# TABLE = CONFIG['tableName']
# SQL = CONFIG['sql_fileName']


'''
HEAD 敏感词字段名
IN_HEAD app、业务、描述信息等字段名
OUT_HEAD ocr结果、敏感词查询结果字段名
DISTINCT_HEAD 主键名
'''
# TABLE_HEAD  = CONFIG['tableHead']


'''
app及业务、国家码
'''
# APP = CONFIG['app']

# BUSINESS = CONFIG['business']

# COUNTRYS = CONFIG['countrys']


'''
OCR_PATH ocr图片文件存放的目录 
'''
OCR_PATH = os.path.join(os.path.join(CURRENT_PATH,".."),"out")


'''
RESULT_PATH 导出excel目录
'''
RESULT_PATH = os.path.join(os.path.join(CURRENT_PATH,".."),"result")


'''
description: 初始化表
param {*}
return {*}
'''
def _init(t, c):
    
    '''
    description: 删除表中所有记录
    param {*} t 表信息
    return {*}
    '''
    def clear_table(t):
        connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
        cursor = connection.cursor()
        sql = """
            delete from {table}
        """.format(table=t['tablename'])
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()

    '''
    description: 如果表不存在则创建表
    param {*} table 表信息
    return {*}
    '''
    def create_table_ine(table):
        engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset={encoding}".format(user=USER,passwd=PASS,host=HOST,port=PORT,db=DB,encoding=CODE))
        con = engine.connect()
        datas = [[]]
        tabledtype = {}
        for k,v in table['tabledtype'].items():
            if v == 'BIGINT':
                tabledtype[k] = BIGINT
            if v == 'TEXT':
                tabledtype[k] = TEXT
            datas[0].append(1)
        df = pd.DataFrame(datas,columns=table['tabledtype'].keys())
        df.to_sql(name=table['tablename'], con=engine, if_exists='append', index=False ,dtype=tabledtype) 
        clear_table(table)

    '''
    description: 判断表是否存在
    param {*} tables 表信息
    return {*} 表是否存在
    '''
    def is_table_exists(tables):
        connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
        cursor = connection.cursor()
        r = []
        for table in tables:
            sql = "show tables;"
            cursor.execute(sql)
            tables = [cursor.fetchall()]
            table_list = re.findall('(\'.*?\')',str(tables))
            table_list = [re.sub("'",'',each) for each in table_list]
            if table['tablename'] in table_list:
                r.append(True)
            else:
                create_table_ine(table)
                r.append(False)
        cursor.close()
        connection.close()
        return r

    t['tablename'] = c['table_name']
    ct = CONFIG_TABLE
    rt = RECORD_TABLE
    smt = SENDMAIL_TABLE
    ot = t
    tables = [ct, rt, smt, ot]
    r = is_table_exists(tables)
    return r



'''
description: 查询ocr需要的所有词
param {*} 
return {*}
'''
def fetchall_data_ocr(c):
    sql = """
        select {fields} from {table} where ocr_word='' ORDER BY RAND()
    """.format(fields=",".join(["word"]), table=c['table_name'])

    connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result



'''
description: 查询敏感词测试要用的所有词
param {*}
return {*}
'''
def fetchall_data_sensitive(c):
    sql = """
        select {fields} from {table} where (word!='' and word_rs='') or (ocr_word!='' and ocr_word_rs='')  ORDER BY RAND()
    """.format(fields=",".join(["id","word","ocr_word"]), table=c['table_name'])

    connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result



'''
description: 从excel读数据
param {*} file 文件路径
param {*} sheet 表名
return {*}
'''
def read_excel_data(file,sheet):
    data = pd.read_excel(file , sheet_name = sheet , dtype={'Stkcd':str})
    data_list = data.values.tolist()
    return data_list



'''
description: 查询所有结果信息
param {*}
return {*} 查询结果
'''
def fetch_result(c):
    sql = """
        select * from {table} where word!='' and ocr_word!='' and word_rs!='' and ocr_word_rs!='' and ocr_word_rs!="['None']" and word_rs!=ocr_word_rs
    """.format(table=c['table_name'])
    connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


'''
description: 导出结果数据到excel
param {*} 
return {*}
'''
def export_datas(c):
    rs = fetch_result(c)
    df = pd.DataFrame(rs)
    export_path = RESULT_PATH
    if "" != c['sql_path'] and None != c['sql_path']:
        export_path = os.path.join(RESULT_PATH, c['sql_path'])
    if not os.path.exists(export_path):
        os.mkdir(export_path)
    export_path = os.path.join(export_path, c['table_name'] + ".xlsx")
    df.to_excel(export_path, sheet_name="Sheet1", header=['rid','cid','经过数据处理的原语料','原语料转换为图片后OCR的识别结果','原语料敏感词查询结果','OCR识别结果的敏感词查询结果'], index=False)
    return export_path


'''
description: 记录信息
param {*} c
param {*} runt
param {*} realt
param {*} finisht
param {*} step
param {*} success
return {*}
'''
def record(c, runt, realt, finisht, step, success):
    connection = pymysql.connect(host=HOST, port=PORT, user=USER,password=PASS, db=DB, charset=CODE)
    cursor = connection.cursor()
    sql = """
        insert into {table}(cid,runtime,realtime,finishtime,step,success) values({cid},'{runtime}','{realtime}','{finishtime}','{step}','{success}')
    """.format(table=RECORD_TABLE['tablename'], cid=c['cid'], runtime=str(runt), realtime=str(realt), finishtime=str(finisht), step=step, success=str(success))
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()


'''
description: 开启jvm
param {*}
return {*}
'''
def start_jvm():
    jar_path = os.path.join(CURRENT_PATH, "inflection_ocr.jar")
    jvmPath = jpype.getDefaultJVMPath() 
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % jar_path)# 启动虚拟机
    

'''
description: 加载图片转换接口
param {*}
return {*} 类
'''
def fetch_jclass():
    demo = jpype.JClass('run/OcrDemo')
    return demo


'''
description: 关闭jvm虚拟机
param {*}
return {*}
'''
def shutdown_jvm():
    jpype.shutdownJVM()


if __name__ == "__main__":
    # rs = fetchall_data_sensitive()
    # for r in rs:
    #     print(r)
    #     pass
    # i = _init()
    # print(i)
    record(c, runt, realt, finisht, step, success)