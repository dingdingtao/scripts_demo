'''
Author: dingdingtao
Date: 2020-12-30 14:27:55
LastEditTime: 2021-01-05 18:41:09
LastEditors: dingdingtao
Description: 从hive跑数据导出到excel
'''
import os
import pandas as pd
from bin import hive_presto
from bin import fetch_config
from bin import fetch_sql

CURRENT_PATH = os.path.dirname(__file__)


'''
description: 导出数据到excel
param {*} config 配置信息
param {*} datas 要写入的数据
return {*}
'''
def export_datas(config, datas):
    try:
        columns = config['excel_columns']
        if 0 == len(columns):
            columns = None
        if 0 == len(datas):
            print("no datas.")
            return False
        df = pd.DataFrame(datas)
        export_path = os.path.join(os.path.join(CURRENT_PATH, "result"), "result - " + str(config['excel_name']))
        df.to_excel(export_path, str(config['excel_sheet']), header=columns, index=False)
        return True
    except Exception as e:
        print(e)
        return False


'''
description: 从hive查数据转存到excel
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
    
    flag = export_datas(config, datas)
    
    if flag:
        print("export success.")

    print("done.")


if __name__ == "__main__":
    run()