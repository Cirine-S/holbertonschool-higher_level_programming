#!/usr/bin/python3
""" get request with error code handling"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.code))
    else:
        print(r.text)
