'''
Author: dingdingtao
Date: 2021-01-11 10:19:01
LastEditTime: 2021-01-11 12:13:40
LastEditors: dingdingtao
Description: 提取词
'''
import re


'''
description: 敏感词匹配
param {*} regexp 正则
param {*} word 敏感词
return {*} r, flag 匹配结果, 是否成功
'''
def extract_findall(regexp, content):
    r = []
    try:
        pattern = re.compile("""%s""" % regexp, re.M|re.I)
        r = pattern.findall(content)

        if r != None and r != []:
            return r, True
    except Exception as e:
        return r, False
    return r, False


'''
description: 
param {*} regexp
param {*} content
return {*}
'''
def extract_split(regexp, content):
    r = []
    try:
        r = re.split(regexp, content)
    except Exception as e:
        return r, False
    return r, True