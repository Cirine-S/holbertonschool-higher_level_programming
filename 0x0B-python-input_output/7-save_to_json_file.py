#!/usr/bin/python3
'''function to serialize in a file'''
import json


def save_to_json_file(my_obj, filename):
    '''function to serialize in a file'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
