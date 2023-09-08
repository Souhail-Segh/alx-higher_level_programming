#!/bin/usr/python3
''' Print a square '''


def print_square(size):
    ''' a function that print a square.
    Args:
    @size: int > 0

    Return: None
    '''

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError('size must be an integer')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for r in range(size):
        for c in range(size):
            print('#', end='')
        print()
