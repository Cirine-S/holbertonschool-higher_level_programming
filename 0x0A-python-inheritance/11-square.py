#!/usr/bin/python3
'''square inherited module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square inherited from Rectangle'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

