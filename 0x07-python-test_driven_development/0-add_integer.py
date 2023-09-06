#!/usr/bin/python3
def add_integer(a, b=98):
    ''' Function that add two integers. '''

    if not (isinstance(a, int) or isinstance(a, float)) \
       or isinstance(a, bool):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
