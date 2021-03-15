'''
Author: dingdingtao
Date: 2020-12-28 11:24:33
LastEditTime: 2021-01-07 09:32:00
LastEditors: dingdingtao
Description: 初始化表结构等
'''
import os
import sys

CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh

'''
description: 调用data_handle init(t, c)方法
param {*} t 
param {*} c
return {*}
'''
def run(t, c):
    try:
        dh._init(t, c)
        return True
    except:
        return False


if __name__ == "__main__":
    run()