#!/usr/bin/python3
'''function to deserialize a string'''
import json


def from_json_string(my_str):
    '''function to deserialize a string'''
    return json.loads(my_str)
