#!/usr/bin/python3
''' function to Append to a file'''


def append_write(filename="", text=""):
    ''' function to Append to a file'''
    with open(filename, 'a') as f:
        return f.write(text)
