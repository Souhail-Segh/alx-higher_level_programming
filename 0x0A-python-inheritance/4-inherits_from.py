#!/usr/bin/python3
'''
Function that check is one obj is instance of another obj
'''


def inherits_from(obj, a_class):
    ''' isinstance function '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
