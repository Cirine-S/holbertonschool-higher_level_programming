#!/usr/bin/python3
import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


f = 'add_item.json'

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

my_list += argv[1:]

save_to_json_file(my_list, f)
