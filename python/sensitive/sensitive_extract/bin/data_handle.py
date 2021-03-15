'''
Author: dingdingtao
Date: 2021-01-11 10:16:39
LastEditTime: 2021-01-11 14:43:09
LastEditors: dingdingtao
Description: 数据处理
'''
import os
import pandas as pd

CURRENT_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(CURRENT_PATH, ".." + os.path.sep + "data")
RESULT_PATH = os.path.join(CURRENT_PATH, ".." + os.path.sep + "result")


def read_data_excel(c):
    alldata = pd.read_excel(os.path.join(DATA_PATH + os.path.sep + c['filename']), sheet_name=c['sheetname'], header=None)
    data_list = alldata.values.tolist()
    data = []
    for d in data_list:
        data.append(d)
    return data



def write_data_excel(c, datas):
    df = pd.DataFrame(datas)
    export_path = os.path.join(RESULT_PATH + os.path.sep + c['filename'])
    df.to_excel(export_path, sheet_name=c['sheetname'], header=None)
    return export_path


def clear_empty(datas):
    reslut = []
    for data in datas:
        if None == data or len(data) == 0:
            continue
        if '\n' == data:
            continue
        if data.strip() in reslut:
            continue
        reslut.append(data)
    return reslut
