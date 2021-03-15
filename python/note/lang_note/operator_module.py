'''
Author: dingdingtao
Date: 2021-01-19 12:03:52
LastEditTime: 2021-01-19 12:07:41
LastEditors: dingdingtao
Description: operator
'''
import operator


def run():
    s1 = "hello"
    s2 = "hello"
    eq = operator.eq(s1, s2)
    '''
    lt 小于
    gt 大于
    eq 等于
    le 小于等于
    ge 大于等于
    ne 不等于
    '''

    print(eq)


if __name__ == "__main__":
    run()