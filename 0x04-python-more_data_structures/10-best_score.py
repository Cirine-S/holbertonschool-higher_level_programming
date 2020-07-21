#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max = 0
        max_key = ''
        for key, value in a_dictionary.items():
            if max < value:
                max = value
                max_key = key
        return (max_key)
