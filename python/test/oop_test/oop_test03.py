'''
Author: dingdingtao
Date: 2021-01-21 15:35:04
LastEditTime: 2021-01-21 15:40:56
LastEditors: dingdingtao
Description: oop test
'''

class Student(object):

    def __init__(self, name, birth):
        self.__name = name
        self.__birth = birth

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, birth):
        self.__birth = birth

    @property
    def age(self):
        return 2021 - self.__birth


if __name__ == "__main__":
    student = Student('dingtao', 1998)
    student.birth = 1999
    print(student.birth)