#!/usr/bin/python3
def print_last_digit(number):
    ldig = abs(number) % 10
    print(ldig, end='')
    return(ldig)
