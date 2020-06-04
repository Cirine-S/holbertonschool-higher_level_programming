#!/usr/bin/python3
'''function to deserialize from a file'''
import json


def load_from_json_file(filename):
    '''function to deserialize from a file'''
    with open(filename) as f:
        return json.load(f)
