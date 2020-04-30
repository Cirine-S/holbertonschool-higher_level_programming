#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = 0
    for i in range(1, len(argv)):
        a += int(argv[i])
    print("{}".format(a))
