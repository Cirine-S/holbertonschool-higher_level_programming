#!/usr/bin/python3
""" A script that fetches URL  """
from urllib import request
import sys


if __name__ == "__main__":
with request.urlopen(sys.argv[1]) as response:
    http_header = response.getheader('X-Request-Id')
    print(http_header)
