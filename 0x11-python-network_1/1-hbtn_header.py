#!/usr/bin/python3
from urllib import request
import sys
''' getheader of X-Request-Id '''


if __name__ == "__main__":
with request.urlopen(sys.argv[1]) as response:
    http_header = response.getheader('X-Request-Id')
print(http_header)
