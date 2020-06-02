#!/usr/bin/python3
"""
check if an obj is an obj of, or if the object is an instance of a class that
inherited from, the same specified class given in arg
"""


def is_same_class(obj, a_class):
    """ check
    """
    return isinstance(obj, a_class)
