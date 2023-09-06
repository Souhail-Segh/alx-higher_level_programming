#!/usr/bin/python3
''' Matrix division '''


def matrix_divided(matrix, div):
    ''' Function that divid a matrix by scalar

    Float/int args


    Raises:

    TypeError: if args' type s are not int/float, \
    or if size of the matrix is not correct

    ZeroDivisionError
    '''
    if not isinstance(matrix, list) or isinstance(matrix, bool):
        raise TypeError('matrix must be a matrix '\
        '(list of lists) of integers/floats')

    size = -1
    nm = []
    for l in matrix:
        if size == -1:
            size = len(l)
        elif size != len(l):
            raise TypeError('Each row of the matrix must have the same size')
        row = []
        for c in l:
            if not isinstance(c,(float, int))or isinstance(c, bool):
                raise TypeError('matrix must be a matrix '\
                '(list of lists) of integers/floats')
            if not isinstance(div,(float, int)):
                raise TypeError('div must be a number')
            if int(div) == 0:
                raise ZeroDivisionError('division by zero')
            res = round(c / div, 2)
            row.append(res)
        nm.append(row)

        if size == -1:
            size = len(l)
        elif size != len(l):
            raise TypeError('Each row of the matrix must have the same size')

    return nm
