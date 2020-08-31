#!/usr/bin/python3
""" get request with error code handling"""
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read().decode()
        print(html)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
