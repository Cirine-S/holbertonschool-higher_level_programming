#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Defines Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantation of width & height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rec += str(self.print_symbol)
            if i == self.height - 1:
                break
            rec += '\n'
        return rec

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
