#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Defines Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Instantation of width & height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """ area """
        return self.height * self.width

    def perimeter(self):
        """ perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return self.height*2 + self.width*2

    def __str__(self):
        """ str """
        if self.width == 0 or self.height == 0:
            return ''
        rec = ''
        for i in range(self.height):
            for j in range(self.width):
                rec += '#'
            rec += '\n'
        return rec
