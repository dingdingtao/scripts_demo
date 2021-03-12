'''
Author: dingdingtao
Date: 2020-12-07 11:31:15
LastEditTime: 2021-03-12 18:50:02
LastEditors: dingdingtao
Description: 
'''
import json
import os



CURRENT_PATH = os.path.dirname(__file__)



'''
description: 获取config.json下指定key对应的value值
param {*} key 要获取的key值
return {*}
'''
def get(key):
    with open(os.path.join(CURRENT_PATH,"config.json"),"r",encoding="utf8") as f:
        config = json.load(f)
    f.close()
    with open(os.path.join(CURRENT_PATH,"_config.json"),"r",encoding="utf8") as f:
        _config = json.load(f)
    f.close()
    try:
        v = config[key]
    except KeyError:
        v = _config[key]
    return v



'''
description: 获取config.json下所有配置参数
param {*}
return {*} dict对象-所有参数key-value
'''
def get_all():
    with open(os.path.join(CURRENT_PATH,"config.json"),"r",encoding="utf8") as f:
        config = json.load(f)
    f.close()
    with open(os.path.join(CURRENT_PATH,"_config.json"),"r",encoding="utf8") as f:
        _config = json.load(f)
    f.close()
    return config, _config



if __name__ == "__main__":
    # config,_config = get_all()
    # print(config,_config)
    v = get('host')
    print(v)