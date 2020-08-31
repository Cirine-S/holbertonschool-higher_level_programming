#!/usr/bin/python3
"""task 1"""
import urllib.request as request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as s:
        r = s.info()
        print(r['X-Request-Id'])
