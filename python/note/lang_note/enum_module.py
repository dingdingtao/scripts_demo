'''
Author: dingdingtao
Date: 2021-02-12 16:55:46
LastEditTime: 2021-02-20 08:59:27
LastEditors: dingdingtao
Description: 枚举
'''
from enum import Enum, unique


Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 从enum继承
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6