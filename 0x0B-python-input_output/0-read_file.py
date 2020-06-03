#!/usr/bin/python3
""" function to read file """


def read_file(filename=""):
    """ function to read file """
    with open(filename) as f:
        reaad = f.read()
    f.closed
    print(reaad, end="")
