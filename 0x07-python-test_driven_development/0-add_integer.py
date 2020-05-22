#!/usr/bin/python3
"""
module that adds 2 integers
"""


def add_integer(a, b=98):
    """ add two integers
    return a + b
    """
    if type(a) not in (float, int):
        raise TypeError("a must be an integer")

    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
