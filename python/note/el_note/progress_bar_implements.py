'''
Author: dingdingtao
Date: 2020-12-24 11:30:38
LastEditTime: 2021-01-06 17:35:30
LastEditors: dingdingtao
Description: 进度条
'''
from tqdm import tqdm
import time
'''
实现进度条的几种方式
https://www.cnblogs.com/huma/p/12198386.html
'''

'''
description: 进度条测试
param {*}
return {*}
'''
def run():
    '''
    for r in tqdm(range(0,100)):
        time.sleep(0.1)
    '''
    try:
        with tqdm([x for x in range(0,100)]) as t:
            time.sleep(0.1)
    except Exception as e:
        print(e)
        t.close()
    t.close()


if __name__ == "__main__":
    run()
