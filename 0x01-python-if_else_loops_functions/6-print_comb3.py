#!/usr/bin/python3
for a in range(80):
    if a / 10 < a % 10:
        print("{:02d}, ".format(a), end='')
print(89)
