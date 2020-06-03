#!/usr/bin/python3
'''Write to a file function'''


def write_file(filename="", text=""):
    '''Write to a file function'''
    with open(filename, mode="w") as f:
        return f.write(text)
