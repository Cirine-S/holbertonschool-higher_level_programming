#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    def area(self):
        """area"""
        return self.__size ** 2

# get & set size
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

# get & set position
    @property
    def position(self):
        """size"""
        return self.__position

    @position.setter
    def position(self, value):
        """position check"""
        if type(value) is not tuple or len(value) is not 2 \
                or not isinstance(value[0], int) \
                or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
