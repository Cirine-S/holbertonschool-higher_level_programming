#!/usr/bin/python3
'''pseudo init module'''


def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
