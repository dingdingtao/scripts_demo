'''
Author: dingdingtao
Date: 2021-01-06 16:53:05
LastEditTime: 2021-01-06 16:55:44
LastEditors: dingdingtao
Description: yield关键字用法
'''

'''
yield关键字用法
https://blog.csdn.net/mieleizhi0522/article/details/82142856/
'''

'''
description: yield关键字测试 
param {*}
return {*}
'''
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)


'''
description: 
param {*}
return {*}
'''
def run():
    g = foo()
    print(next(g))
    print("*"*20)
    print(next(g))
    pass 


if __name__ == "__main__":
    run()