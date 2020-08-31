#!/usr/bin/python3
""" http header request """
import requests
import sys


if __name__ == "__main__":
    http_header = requests.get(sys.argv[1])
    print(http_header.headers.get('X-Request-Id'))
