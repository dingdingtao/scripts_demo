'''
Author: dingdingtao
Date: 2021-01-21 12:25:52
LastEditTime: 2021-01-21 15:13:03
LastEditors: dingdingtao
Description: oop test
'''

class Person(object):
    
    person_count = 0

    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age
        Person.person_count += 1
    
    def __del__(self):
        Person.person_count -= 1

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age
    
    def say(self):
        print("class person ", self.__name)

    def get_attr_dict(self):
        return {'name':self.__name,'gender':self.__gender,'age':self.__age}

    def print_attr(self):
        print("name:{name}, gender:{gender}, age:{age}".format(name=self.__name, gender=self.__gender, age=self.__age))



if __name__ == "__main__":
    person = Person('dingtao', 'female', 22)
    attr_dict = person.get_attr_dict()

    print(attr_dict['name'])

    print(person.__dict__)
    print(person._Person__name)
    person.print_attr()
    
    person1 = Person('dingtao1', 'female', 22)

    print("person_count:", Person.person_count)