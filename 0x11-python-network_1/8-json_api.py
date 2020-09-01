#!/usr/bin/python3
""" take in a letter and send a POST request with that letter as param"""
import requests
import sys


if __name__ == "__main__":
    if sys.argv[1]:
        dicti = {'q': sys.argv[1]}
    else:
        dicti = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', dicti)

    try:
        f = r.json()
        if len(f) > 0:
            print("[{}] {}".format(f['id'], f['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
