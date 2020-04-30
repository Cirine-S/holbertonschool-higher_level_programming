#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print ("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = ['+', '-', '*', '/']
    if argv[2] not in op:
        print ("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        res = add(a, b)
    elif argv[2] == '-':
        res = sub(a, b)
    elif argv[2] == '*':
        res = mul(a, b)
    else:
        res = div(a, b)

    print("{} {} {} = {}".format(a, argv[2], b, res))
