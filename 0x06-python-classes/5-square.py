#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """init"""
        self.size = size

    def area(self):
        """area"""
        return self.__size ** 2

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size check"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
