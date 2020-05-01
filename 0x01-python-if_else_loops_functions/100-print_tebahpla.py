#!/usr/bin/python3
i = ord('z')
while i >= ord('a'):
    if i % 2 == 0:
        print(chr(i), end='')
    else:
        print(chr(i-32), end="")
    i -= 1
