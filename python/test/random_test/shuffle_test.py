'''
Author: dingdingtao
Date: 2021-01-26 12:36:03
LastEditTime: 2021-01-26 12:38:54
LastEditors: dingdingtao
Description: shuffle
'''
import random


def run():
    '''
    shuffle() 方法将序列的所有元素随机排序。
    '''

    l = [1,2,3,4,5,6,7,8,9,0]
    '''打乱顺序'''
    random.shuffle(l)
    print(l)

if __name__ == "__main__":
    run()
    pass