#!/usr/bin/python3
""" post request """
from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode())
