#!/usr/bin/python3
""" get request with error code handling"""
from urllib.error import HTTPError
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            html = response.read().decode()
        print(html)
    except HTTPError as r:
        print('Error code: {}'.format(r.code))
