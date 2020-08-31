#!/usr/bin/python3
import urllib.request as request
import sys
''' getheader of X-Request-Id '''


with request.urlopen(sys.argv[1]) as response:
    http_header = response.getheader('X-Request-Id')
print(http_header)
