#!/usr/bin/python3
""" take in a letter and send a POST request to a URL with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
