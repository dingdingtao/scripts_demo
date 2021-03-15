'''
Author: dingdingtao
Date: 2021-01-21 12:46:44
LastEditTime: 2021-01-21 15:25:09
LastEditors: dingdingtao
Description: oop test
'''
from oop_test01 import Person


class Worker(Person):

    def __init__(self, name, gender, age):
        super(Worker, self).__init__(name, gender, age)
        self.__name = name
        self.__gender = gender
        self.__age = age

    def work(self):
        print("{worker_name} work hard.".format(worker_name=self.__name))
    
    def say(self):
        print("class worker", self.__name)



if __name__ == "__main__":
    '''实例化一个Worker'''
    worker = Worker('dingtao', 'female', '22')
    worker.work()
    worker.say()
    worker_name = worker.get_name()
    worker_age_v1 = worker.get_age()
    worker.set_age('23')
    worker_age_v2 = worker.get_age()
    print("worker_name:", worker_name)
    print("worker_age_v1:", worker_age_v1)
    print("worker_age_v2:", worker_age_v2)

    '''实例化另一个Worker'''
    worker1 = Worker('dingtao1', 'male', '23')
    print(Worker.person_count)