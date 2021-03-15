'''
Author: dingdingtao
Date: 2020-12-22 11:53:46
LastEditTime: 2021-01-07 09:30:33
LastEditors: dingdingtao
Description: 导出数据
'''
import os
import sys


'''
引入data_handle模块查询数据
'''
CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh


'''
description: 导出所有数据
param {*}
return {*}
'''
def export_result(c):
    export_path = dh.export_datas(c)
    return export_path
        

'''
description: 导出数据
param {*} c 配置信息
return {*} 是否导出成功
'''
def run(c):
    print("导出数据.")
    try:
        export_path = export_result(c)
        print("导出成功.")
        return True, export_path
    except Exception as e:
        print("导出失败.")
        print(e)
        return False, export_path


if __name__ == "__main__":
    run()
    