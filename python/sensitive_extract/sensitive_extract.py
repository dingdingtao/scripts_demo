'''
Author: dingdingtao
Date: 2021-01-07 16:00:12
LastEditTime: 2021-03-12 18:59:42
LastEditors: dingdingtao
Description: 提取敏感词
'''
import os
import json
from bin import data_handle
from bin import extract_handle

CURRENT_PATH = os.path.dirname(__file__)

'''
description: 读取配置文件
param {*}
return {*} 配置信息
'''
def get_config():
    with open(os.path.join(CURRENT_PATH,"config\\config.json"),"r",encoding="utf8") as f:
        config = json.load(f)
    f.close()
    return config


'''
description: list形式正则
param {*}
return {*}
'''
def extract_list():
    config = get_config()
    datas = data_handle.read_data_excel(config)
    result = []
    sep_extract1 = "(?<=\[[\'|\"]).+(?=[\'|\"]\])"
    sep_extract2 = "[\'|\"], [\'|\"]"
    for data in datas:
        r, f = [], False
        r1, f1 = [], False
        r2, f2 = [], False
        '''去除括号'''
        r1, f1 = extract_handle.extract_findall(sep_extract1, str(data[config['regexp_col']]))
        if f1:
            '''分割正则'''
            for _r1 in r1:
                r2, f2 = extract_handle.extract_split(sep_extract2, _r1)
        _temp = [x for x in data]
        temp = []
        '''提取词'''
        for _r2 in r2:
            r, f = extract_handle.extract_findall(_r2, data[config['content_col']])
            t = []
            try:
                for _r in r[0]:
                    if _r not in [' ','-','\n','\"','\'']:
                        t.append(_r)
                    else:
                        t.append("")
            except Exception as e:
                pass
            temp = temp + ["".join(t)]
            if None == temp:
                temp = []
        temp = data_handle.clear_empty(temp)
        print(temp)
        _temp = _temp + [",".join(temp)]
        result.append(_temp)
        data_handle.write_data_excel(config, result)


'''
description: 提取单个
param {*}
return {*}
'''
def extract_single():
    datas = data_handle.read_data_excel(config)
    result = []
    for data in datas:
       r, f = extract_handle.extract_findall(data[config['regexp_col']], data[config['content_col']])
       result = result + [",".join(r)]
    data_handle.write_data_excel(config, result)



'''
description: 
param {*}
return {*}
'''
def run():
    extract_list()


if __name__ == "__main__":
    run()