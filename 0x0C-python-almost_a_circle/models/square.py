#!/usr/bin/python3
from models.rectangle import Rectangle
'''square module'''


class Square(Rectangle):
    '''inherited square class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        ''' size property'''
        return self.width

    @size.setter
    def size(self, size):
        '''size setter'''
        self.width = size
        self.height = size

    def __str__(self):
        """ str """
        return "[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update"""
        if len(args) > 0:
            self.id = args[0]
        elif "id" in kwargs:
            self.id = kwargs["id"]

        if len(args) > 1:
            self.size = args[1]
        elif "size" in kwargs:
            self.size = kwargs["size"]

        if len(args) > 2:
            self.x = args[2]
        elif "x" in kwargs:
            self.x = kwargs["x"]

        if len(args) > 3:
            self.y = args[3]
        elif "y" in kwargs:
            self.y = kwargs["y"]
