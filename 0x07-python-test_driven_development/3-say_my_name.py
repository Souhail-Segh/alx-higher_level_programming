#!/usr/bin/python3
''' Say my name '''


def say_my_name(first_name, last_name=""):
    ''' Function that concatenate two strings. '''
    '''
    print(first_name + last_name)
    print(type(first_name))
    print(not isinstance(first_name, str))
    print(not isinstance(last_name, str))
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    space = ' '
    if last_name == '':
        space = ''
    print('My name is {}{}{}'.format(first_name, space, last_name))
