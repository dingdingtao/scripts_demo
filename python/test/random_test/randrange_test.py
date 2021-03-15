'''
Author: dingdingtao
Date: 2021-01-26 12:33:30
LastEditTime: 2021-01-26 12:34:51
LastEditors: dingdingtao
Description: randrange
'''
import random


def run():
    '''
    randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    '''

    # 输出 100 <= number < 1000 间的偶数
    print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))

    # 输出 100 <= number < 1000 间的其他数
    print("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))


if __name__ == "__main__":
    run()