#!/usr/bin/python3
'''rectangle file'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Rectangle __init__'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Rectangle __str__'''
        return ("[Rectangle] (%s) %s/%s - %s/%s" % (
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
            ))

    def area(self):
        '''area function'''
        return (self.__width * self.__height)

    def display(self):
        '''display function'''
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(end=" ")
            for _ in range(self.__width):
                print(end="#")
            print()

    def update(self, *args, **kwargs):
        '''update function'''
        if "id" in kwargs:
            self.id = kwargs["id"]
        elif len(args) > 0:
            self.id = args[0]
        if "width" in kwargs:
            self.width = kwargs["width"]
        elif len(args) > 1:
            self.width = args[1]
        if "height" in kwargs:
            self.height = kwargs["height"]
        elif len(args) > 2:
            self.height = args[2]
        if "x" in kwargs:
            self.x = kwargs["x"]
        elif len(args) > 3:
            self.x = args[3]
        if "y" in kwargs:
            self.y = kwargs["y"]
        elif len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        '''to_dictionary function'''
        dicti = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return (dicti)

    @property
    def width(self):
        '''width property'''
        return self.__width

    @property
    def height(self):
        '''height property'''
        return self.__height

    @property
    def x(self):
        '''x property'''
        return self.__x

    @property
    def y(self):
        '''y property'''
        return self.__y

    @width.setter
    def width(self, value):
        '''width Setter'''
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        '''height Setter'''
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, value):
        '''x Setter'''
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, value):
        '''y Setter'''
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
