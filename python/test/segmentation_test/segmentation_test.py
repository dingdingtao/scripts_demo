'''
Author: dingdingtao
Date: 2021-01-19 11:21:17
LastEditTime: 2021-01-19 11:48:53
LastEditors: dingdingtao
Description: 
'''
import os
import sys
import paddlehub as hub

# 1.加载模型
humanseg = hub.Module(name="deeplabv3p_xception65_humanseg")

# 2.指定待抠图图片目录
path = './source/'
files = []
dirs = os.listdir(path)
for diretion in dirs:
    files.append(path + diretion)
    print(path + diretion)

# 3.抠图
results = humanseg.segmentation(data={"image": files})

for result in results:
    print(result)
    # print(result['origin'])
    # print(result['processed'])