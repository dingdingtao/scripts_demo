'''
Author: dingdingtao
Date: 2020-12-07 22:29:26
LastEditTime: 2020-12-07 22:56:00
Description: json
'''
import json


'''
Description: 
param {*}
return {*}
'''
def json_module():
    '''
    dumps   : 把python对象转换为json格式字符串
    '''

    dumps_data = {"test1":1,"test2":"abc"}
    dumps = json.dumps(dumps_data)

    dumps_data_type = type(dumps_data)
    dumps_type = type(dumps)
    print(print_data(dumps_data, dumps_data_type, dumps, dumps_type))
    


    '''
    loads   : 把json字符串转换为python对象
    '''

    loads_data = r"{'test1':'1','test2':'abc'}"
    loads = json.loads(loads_data)

    loads_data_type = type(loads_data)
    loads_type = type(loads)
    print(print_data(loads_data, loads_data_type, loads, loads_type))



    '''
    dump   : 把python对象转换为json格式字符串
    load   : 把json字符串转换为python对象
    '''


    '''
        object	        dict
        array	        list
        string	        unicode
        number (int)	int, long
        number (real)	float
        true	        True
        false	        False
        null	        None
    '''



def print_data(dumps_data,dumps_data_type,dumps,dumps_type):
    printf = """
    原数据:{}   -   type:{}
    转换后:{}   -   type:{}
    """.format(dumps_data,dumps_data_type,dumps,dumps_type)
    return printf


if __name__ == "__main__":
    json_module()