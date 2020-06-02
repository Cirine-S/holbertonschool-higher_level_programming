#!/usr/bin/python3
"""
check if an obj is an inheritance of a specified super class
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
