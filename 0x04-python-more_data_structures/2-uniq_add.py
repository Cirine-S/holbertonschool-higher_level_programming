#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for x in new_list:
        sum += x
    return sum
