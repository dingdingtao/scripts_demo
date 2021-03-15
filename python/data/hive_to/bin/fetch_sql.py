'''
Author: dingdingtao
Date: 2020-12-30 14:35:28
LastEditTime: 2021-01-01 21:03:28
LastEditors: dingdingtao
Description: 读取sql文件
'''
import os

CURRENT_PATH = os.path.dirname(__file__)


'''
Description: 读取sql
param {*} config 配置信息,sql文件路径
return {*} sql语句
'''
def fetch(config):
    sqlfile = open(CURRENT_PATH+'\\..\\sql\\' + config['sql'], 'r', encoding = 'utf8')
    sqltxt = sqlfile.readlines()
    sqlfile.close()
    sql = "".join(sqltxt)
    return sql