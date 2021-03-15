'''
Author: dingdingtao
Date: 2021-01-04 14:32:16
LastEditTime: 2021-01-04 14:38:33
LastEditors: dingdingtao
Description: 
'''
import os

def path_test():
    #当前文件路径 包含文件名
    CURRENT_FILEPATH = os.path.abspath(__file__)
    #当前文件所在文件夹
    CURRENT_DIRPATH = os.path.abspath(os.path.dirname(CURRENT_FILEPATH) + os.path.sep + ".")
    pp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "aaaff" + os.path.sep + "aaaa")
    print(pp)
    print(CURRENT_FILEPATH)
    print(CURRENT_DIRPATH)
    print('\\\"')





