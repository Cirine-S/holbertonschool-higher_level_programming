#!/usr/bin/python3
'''rectangle module'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle subclass'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "[Rectangle] " + str(self.width) + "/" + str(self.height)
