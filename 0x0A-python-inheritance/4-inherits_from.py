#!/usr/bin/python3
'''
Function that check is one obj is instance of another obj
'''


def is_kind_of_class(obj, a_class):
    ''' isinstance function '''

    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    else:
        return False
