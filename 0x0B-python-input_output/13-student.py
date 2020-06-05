#!/usr/bin/python3
'''class module'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return self.__dict__

        dict = {}
        for item in attrs:
            if type(item) is not str:
                return self.__dict__
            if item in self.__dict__:
                dict[item] = self.__dict__[item]
        return dict

    def reload_from_json(self, json):
        for attr in self.json[attr]:
            self.__dict__[attr] = json[attr]
