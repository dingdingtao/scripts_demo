'''
Author: dingdingtao
Date: 2021-01-26 12:27:36
LastEditTime: 2021-01-26 12:30:28
LastEditors: dingdingtao
Description: choice
'''
import random

def run():
    '''
    choice() 方法返回一个列表，元组或字符串的随机项。
    '''

    rand_int = random.choice([1,2,3,4,5,6,7,8,9,0])

    rand_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    print(rand_int,rand_char)


if __name__ == "__main__":
    run()
