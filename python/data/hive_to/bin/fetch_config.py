'''
Author: dingdingtao
Date: 2020-12-30 14:40:08
LastEditTime: 2021-01-01 21:02:32
LastEditors: dingdingtao
Description: 读取配置文件
'''
import os
import json

CURRENT_PATH = os.path.dirname(__file__)

'''
Description: 读取配置文件
param {*}
return {*} config 常用配置, _config 固定配置
'''
def fetch():
    with open(os.path.join(CURRENT_PATH,".." + os.path.sep + "config" + os.path.sep + "config.json"),"r",encoding="utf8") as f:
        config = json.load(f)
    f.close()
    with open(os.path.join(CURRENT_PATH,".." + os.path.sep + "config" + os.path.sep + "_config.json"),"r",encoding="utf8") as f:
        _config = json.load(f)
    f.close()
    return config, _config