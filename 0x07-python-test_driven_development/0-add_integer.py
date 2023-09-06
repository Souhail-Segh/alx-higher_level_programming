#!/usr/bin/python3
''' Function that add two integers. '''


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if not (isinstance(a, int) or isinstance(a, float)) \
       or isinstance(a, bool):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
