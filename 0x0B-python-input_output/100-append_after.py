#!/usr/bin/python3
'''insert a line of text to a file in a specific place module'''


def append_after(filename="", search_string="", new_string=""):
    '''insert function'''
    s = ''
    with open(filename, 'r') as f:
        for line in f:
            s += line
            if search_string in line:
                s += new_string

    with open(filename, 'w') as f:
        f.write(s)
