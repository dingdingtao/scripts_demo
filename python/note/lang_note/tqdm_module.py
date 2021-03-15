'''
Author: dingdingtao
Date: 2020-12-22 14:41:58
LastEditTime: 2020-12-24 11:31:49
LastEditors: dingdingtao
Description: tqdm进度条
'''
from tqdm import tqdm
import time


'''
iterable=None,            
desc=None,      传入str类型，作为进度条标题（类似于说明）
total=None,     预期的迭代次数
leave=True,             
file=None, 
ncols=None,         可以自定义进度条的总长度
mininterval=0.1,    最小的更新间隔
maxinterval=10.0,   最大更新间隔
miniters=None, 
ascii=None, 
unit='it',          单位
unit_scale=False, 
dynamic_ncols=False, 
smoothing=0.3,
bar_format=None, 
initial=0, 
position=None, 
postfix             以字典形式传入 详细信息 例如  速度= 10，
'''

for i in tqdm(range(1000)):
    time.sleep(0.05)