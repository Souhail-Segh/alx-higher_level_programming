#!/usr/bin/python3
'''
Function that check is one obj is instance of another obj
'''


def is_same_class(obj, a_class):
    ''' isinstance function '''
    if (type(a_class) == obj):
        return True
    return False
