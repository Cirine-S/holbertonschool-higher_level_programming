#!/usr/bin/python3
""" returns all properties and methods of the specified object,
without the values"""


def lookup(obj):
    """ return a list object """
    return (dir(obj))
