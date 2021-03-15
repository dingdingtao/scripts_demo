'''
Author: dingdingtao
Date: 2021-02-02 14:30:42
LastEditTime: 2021-03-03 15:46:17
LastEditors: dingdingtao
Description: hive查询并输出查询结果
'''
import os
from bin import hive_presto

CURRENT_PATH = os.path.dirname(__file__)

def run():
    sql = ''
    with open(os.path.join(CURRENT_PATH,'sql' + os.path.sep + 'test.sql'),'r',encoding='utf-8') as f:
        sql = f.read()
    f.close()
    # datas = hive_presto.hive_presto_sg_sql(sql)
    datas = hive_presto.hive_presto_sql(sql)
    for data in datas:
        print(data)


if __name__ == '__main__':
    run()