#!/usr/bin/python3
""" function to read lines """


def number_of_lines(filename=""):
    """ function to read lines """
    with open(filename) as f:
        count = len(f.readlines())
    f.closed
    return count
