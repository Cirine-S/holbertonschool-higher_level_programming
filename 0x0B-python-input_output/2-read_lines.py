#!/usr/bin/python3
""" function to read a given number of lines"""


def read_lines(filename="", nb_lines=0):
    """ function to read a given number of lines"""
    count = 0
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
