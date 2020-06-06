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
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __gt__(self, other):
        return self.__size > other.__size
