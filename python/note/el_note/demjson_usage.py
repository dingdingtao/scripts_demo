'''
Author: dingdingtao
Date: 2020-12-07 22:56:18
LastEditTime: 2020-12-07 22:59:18
Description: demjson json解析
'''
import demjson


'''
Description: 
param {*}
return {*}
'''
def demjson_usage():
    '''
    encode(self, obj, nest_level=0) 函数用于将 Python 对象编码成 JSON 字符串。
    decode(self, txt) 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。
    '''


    '''
    encode
    '''
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

    json = demjson.encode(data)
    print(json)
    

    '''
    decode
    '''
    json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

    text = demjson.decode(json)
    print(text)
