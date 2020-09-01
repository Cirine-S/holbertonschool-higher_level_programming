#!/usr/bin/python3
""" takes my Github credentials & display my id """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, pwd))
    print(r.json().get('id'))
