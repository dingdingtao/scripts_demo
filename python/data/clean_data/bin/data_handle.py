'''
Author: dingdingtao
Date: 2021-01-06 22:09:51
LastEditTime: 2021-01-15 12:04:28
LastEditors: dingdingtao
Description: 数据处理
'''
import re


'''
description: 处理emoji
param {*} data 原数据
return {*} _data 处理后的数据
'''
def clean_emoji(data):
    '''emoji正则待完善'''
    emoji_pattern = re.compile(u'[\U0001F680-\U0001F6FF]|[\U0001F300-\U0001F64F]|[\u2600-\u2B55]')
    _data = re.sub(emoji_pattern, '', data)
    return _data



'''
description: 处理特殊符号
param {*} data 原数据
return {*} _data 处理后的数据
'''
def clean_symbol(data):
    symbol_pattern = re.compile(u'[,𓊈𓊉«\{\{.;`~!@#$%^&*()+=|\{\}\':;\',\\\"[\\].<>/?~！@#￥%……&*（）——+|\{\}【】‘；：”“’。，、？]')
    _data = re.sub(symbol_pattern, '', data)
    return _data
