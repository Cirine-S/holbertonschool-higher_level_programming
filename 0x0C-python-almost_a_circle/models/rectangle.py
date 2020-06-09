#!/usr/bin/python3
'''inherited Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''inherited class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''init constructor'''
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# properties

    @property
    def width(self):
        '''width property'''
        return self.__width

    @width.setter
    def width(self, width):
        '''width setter'''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        '''height property'''
        return self.__height

    @height.setter
    def height(self, height):
        '''height setter'''
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        '''x propertyyyyyy'''
        return self.__x

    @x.setter
    def x(self, x):
        '''x setterrrrr'''
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        '''y propertyyyyyy'''
        return self.__y

    @y.setter
    def y(self, y):
        '''y setterrrrrrrrrrrr'''
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''area'''
        return self.__width * self.__height

    def display(self):
        '''display'''
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        '''str'''
        return "[Rectangle] ({}) {}/{} - \
{}/{}".format(self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''update'''
        if len(args) > 0:
            self.id = args[0]
        elif "id" in kwargs:
            self.id = kwargs["id"]

        if len(args) > 1:
            self.width = args[1]
        elif "width" in kwargs:
            self.width = kwargs["width"]

        if len(args) > 2:
            self.height = args[2]
        elif "height" in kwargs:
            self.height = kwargs["height"]

        if len(args) > 3:
            self.x = args[3]
        elif "x" in kwargs:
            self.x = kwargs["x"]

        if len(args) > 4:
            self.y = args[4]
        elif "y" in kwargs:
            self.y = kwargs["y"]
