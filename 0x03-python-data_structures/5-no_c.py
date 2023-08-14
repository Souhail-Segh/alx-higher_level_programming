#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for s in my_string:
        if s not in ['c', 'C']:
            new_string = new_string + s
    return new_string
