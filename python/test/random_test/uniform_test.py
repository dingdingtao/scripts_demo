'''
Author: dingdingtao
Date: 2021-01-26 15:16:46
LastEditTime: 2021-01-26 15:20:02
LastEditors: dingdingtao
Description: uniform
'''
import random


def run():
    '''
    uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
    返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。
    '''
    r = random.uniform(5,15)
    print(r)


if __name__ == "__main__":
    run()
