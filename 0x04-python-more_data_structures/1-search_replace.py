#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in new_list:
        if i + 1 == search:
            new_list[i] = replace
    return new_list
