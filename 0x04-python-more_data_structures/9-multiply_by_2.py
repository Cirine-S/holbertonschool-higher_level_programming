#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdictionary = {}
    for key in a_dictionary:
        newdictionary[key] = a_dictionary[key] * 2
    return newdictionary
