#!/usr/bin/python3
""" A script that fetches URL  """
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as s:
        r = s.info()
        print(r['X-Request-Id'])
