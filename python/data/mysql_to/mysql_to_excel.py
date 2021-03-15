'''
Author: dingdingtao
Date: 2020-12-30 19:20:51
LastEditTime: 2021-01-06 15:19:25
LastEditors: dingdingtao
Description: 从mysql导出到excel
'''
import os
import pandas
from bin import fetch_config
from bin import fetch_sql
from bin import fetch_data

CURRENT_PATH = os.path.dirname(__file__)


'''
description: 导出数据到excel
param {*} config 配置信息
param {*} datas 要写入的数据
return {*} export_path, flag 导出文件路径, 是否成功
'''
def export_datas(config, datas):
    try:
        columns = config['excel_columns']
        if 0 == len(columns):
            columns = None
        if 0 == len(datas):
            print("no datas.")
            return "", False
        df = pandas.DataFrame(datas)
        export_path = os.path.join(os.path.join(CURRENT_PATH, "result"), "result - " + str(config['excel_name']))
        df.to_excel(export_path, str(config['excel_sheet']), header=columns, index=False)
        return export_path, True
    except Exception as e:
        print(e)
        return "", False


'''
Description: 
param {*}
return {*}
'''
def run():
    '''获取配置信息'''
    config, _config = fetch_config.fetch()

    '''读取sql语句'''
    sql = fetch_sql.fetch(config)

    '''从mysql查询数据'''
    datas, datas_flag = fetch_data.fetch_all(_config, sql)
    if datas_flag:
        export_path,export_flag = export_datas(config, datas)
        if export_flag:
            print(str(export_path))
        else:
            print("export failed.")
    else:
        print("fetch data failed.")


if __name__ == "__main__":
    run()