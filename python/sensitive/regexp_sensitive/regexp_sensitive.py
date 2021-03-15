'''
Author: dingdingtao
Date: 2020-12-30 10:54:00
LastEditTime: 2021-01-07 10:30:07
LastEditors: dingdingtao
Description: 敏感词-正则匹配
'''
import re
import os
import json
from bin import data_handle

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
description: 敏感词匹配
param {*} regexp 正则
param {*} word 敏感词
return {*} r, flag 匹配结果, 是否成功
'''
def sensitive_match(regexp,word):
    r = re.search("""%s""" % regexp,word, re.M|re.I)
    if r != None:
        return regexp, True
    return r, False



if __name__ == "__main__":
    '''读取配置文件'''
    config = get_config()
    '''清空数据表'''
    data_handle.clear_table(config)
    '''把数据转存到mysql'''
    datas = data_handle.fetch_data_mysql(config)
    '''把正则转存到mysql'''
    regexps = data_handle.fetch_regexp_mysql(config)
    result = []
    for di,data in enumerate(datas):
        wid = data[0]
        word = data[1]
        for ri,regexp in enumerate(regexps):
            rid = regexp[0]
            reg = regexp[1]
            '''匹配敏感词 用正则去匹配所有词'''
            r, f = sensitive_match(reg,word)
            '''如果匹配不成功或没有结果则不生成记录'''
            if r == None and not f:
                continue
            row = [di, ri, word, r, f]
            # print(row)
            result.append(row)
    '''导出数据'''
    data_handle.export_datas(config, result)