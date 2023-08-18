#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    div = 0
    for s, w in my_list:
        average += w * s
        div += w
    if div == 0:
        return 0
    average /= div
    return average
