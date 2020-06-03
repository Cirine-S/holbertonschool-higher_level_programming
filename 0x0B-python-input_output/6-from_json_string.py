#!/usr/bin/python3
'''function to deserialize a string'''


def from_json_string(my_str):
    '''function to deserialize a string'''
    return json.load(my_str)
