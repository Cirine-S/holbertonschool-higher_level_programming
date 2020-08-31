#!/usr/bin/python3
""" post request """
import requests
import sys


if __name__ == "__main__":
    dicti = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=dicti)
    print(r.text)
