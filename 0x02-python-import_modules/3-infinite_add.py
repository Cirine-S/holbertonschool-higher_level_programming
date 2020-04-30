#!/usr/bin/python3
from sys import argv
a = 0
for i in range(1, len(argv)):
    a += int(argv[i])
print("{}".format(a))
