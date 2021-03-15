'''
Author: dingdingtao
Date: 2021-01-06 21:59:11
LastEditTime: 2021-03-15 12:44:50
LastEditors: dingdingtao
Description: 数据清洗
'''
from bin import data_handle as handle


'''
description: 从文件读数据
param {*}
return {*}
'''
def read_data_file():
    pass



def run():
    data = ""

    '''emoji'''
    handle_data = handle.clean_emoji(data)
    
    '''特殊符号'''
    handle_data = handle.clean_symbol(data)

    print(handle_data)