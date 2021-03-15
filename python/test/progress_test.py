'''
Author: dingdingtao
Date: 2021-01-20 10:19:05
LastEditTime: 2021-01-20 10:19:06
LastEditors: dingdingtao
Description: 
'''
import time  # 导入time模块

length = 100  # 定义长度变量
for i in range(1, length + 1):  # 循环遍历1~100中的数
    percentage = i / length  # 求进度条的百分比
    block = "#" * int(i // (length / 20))  # 计算进度条的个数
    time.sleep(0.1)  # 休眠0.1秒 ==> 即线程挂起0.1秒
    # 格式化输出 ==> :<20 左对齐 宽度为20 :>6.1% 保留1位小数的六位百分数
    print("\r 加载条: |{:<20}|{:>6.1%}".format(block, percentage), end="")