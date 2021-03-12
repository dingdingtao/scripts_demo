'''
Author: dingdingtao
Date: 2020-12-18 12:41:05
LastEditTime: 2021-03-12 18:39:41
LastEditors: dingdingtao
Description: 清洗数据
'''
import re
import emoji


'''
description: 数据清洗
param {*} content 要清洗的数据
return {*} 清洗过后的数据
'''
def regular_filtering(content):
    emoji_pattern = re.compile(u'[\U0001F680-\U0001F6FF]|[\U0001F300-\U0001F64F]|[\u2600-\u2B55]')
    bengali_pattern = re.compile(u'[\u0980-\u09FF]')
    symbol_pattern = re.compile(u'[,𓊈𓊉«\{\{.;`~!@#$%^&*()+=|\{\}\':;\',\\\"[\\].<>/?~！@#￥%……&*（）——+|\{\}【】‘；：”“’。，、？]')
    zh_pattern = re.compile(u'[\u4e00-\u9fa5a-zA-Z0-9x0400-x052f\“\”]+')
    
    match = re.sub(emoji_pattern, '', content)
    match = re.sub(bengali_pattern, '', match)
    match = re.sub(symbol_pattern, '', match)

    return match


if __name__ == "__main__":
    filtering_word = regular_filtering("🎸aaaa🎸")
    print(filtering_word)