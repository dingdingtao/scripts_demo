'''
Author: dingdingtao
Date: 2021-01-21 16:08:44
LastEditTime: 2021-01-21 16:11:55
LastEditors: dingdingtao
Description: oop test
'''

'''引入枚举类Enum'''
from enum import Enum, unique


'''确保枚举值唯一'''
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == "__main__":
    day1 = Weekday.Mon
    print(day1)

    Weekday.Mon
    print(Weekday.Tue)

    Weekday.Tue
    print(Weekday['Tue'])

    Weekday.Tue
    print(Weekday.Tue.value)

    print(day1 == Weekday.Mon)

    print(day1 == Weekday.Tue)

    print(Weekday(1))

    print(day1 == Weekday(1))
    
    try:
        print(Weekday(7))
    except Exception as e:
        print('-' * 20)
        print(e)