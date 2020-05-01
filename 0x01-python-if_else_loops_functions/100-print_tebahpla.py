#!/usr/bin/python3
i = ord('z')
while i >= ord('a'):
    if i % 2 == 0:
        c = chr(i)
    else:
        c = chr(i-32)
    print(c, end="")
    i -= 1
