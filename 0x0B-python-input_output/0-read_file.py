#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        reaad = f.read()
    f.closed
    print(reaad, end="")
