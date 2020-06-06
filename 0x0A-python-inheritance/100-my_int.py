#!/usr/bin/python3
'''MyInt inherited from int module'''


class MyInt(int):
    '''rebel subclass'''
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
