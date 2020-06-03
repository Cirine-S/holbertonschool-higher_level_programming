#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as f:
        count = len(f.readlines(  ))
    f.closed
    return count
