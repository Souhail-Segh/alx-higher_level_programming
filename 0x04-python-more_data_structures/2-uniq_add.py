#!/usr/bin/python3
def uniq_add(my_list=[]):
    a_set = set(my_list)
    sum = 0
    for a in a_set:
        sum += a
    return sum
