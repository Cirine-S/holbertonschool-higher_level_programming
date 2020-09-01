#!/usr/bin/python3
'''list 10 last commits'''
import requests
import sys


if __name__ == "__main__":
    URL = "https://api.github.com/repos/"
    URL += sys.argv[2] + "/" + sys.argv[1] + "/commits"
    r = requests.get(URL)
    dicti = r.json()
    try:
        for i in range(10):
            id = dicti[i].get("sha")
            name = dicti[i].get("commit").get("author").get("name")
            print("{}: {}".format(id, name))
    except:
        pass
