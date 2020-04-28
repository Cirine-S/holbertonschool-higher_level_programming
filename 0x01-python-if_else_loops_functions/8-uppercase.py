#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print("{:c}".format(ord(str[i]) - num), end='')
        else:
            print("{:c}".format(str[i]), end='')
    print()
