#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''square inherited module'''


class Square(Rectangle):
    '''square inherited from Rectangle'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
