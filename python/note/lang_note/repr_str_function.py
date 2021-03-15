'''
Author: dingdingtao
Date: 2021-01-27 11:44:24
LastEditTime: 2021-01-27 12:19:58
LastEditors: dingdingtao
Description: str&repr函数
'''

def str_run():
    str_str = "'hello world'"
    print(repr(str_str))
    str_str = 'hello world'
    print(repr(str_str))

    str_dict = {'hello': 'Hello', 'world': 'World'}
    print(repr(str_dict))
    str_dict = {'hello': "Hello", "world'": 'World'}
    print(repr(str_dict))
    pass



def repr_run():
    repr_str = "'hello world'"
    print(repr(repr_str))
    repr_str = 'hello world'
    print(repr(repr_str))

    repr_dict = {'hello': 'Hello', 'world': 'World'}
    print(repr(repr_dict))
    repr_dict = {'hello': "Hello", "world'": 'World'}
    print(repr(repr_dict))
    pass



def run():
    
    pass


if __name__ == "__main__":
    str_run()
    print('*'*20)
    repr_run()