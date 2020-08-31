#!/usr/bin/python3
''' finds a peak of a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' finds a peak of a list of unsorted integers '''
    if list_of_integers == []:
        return None
    return max(list_of_integers)
