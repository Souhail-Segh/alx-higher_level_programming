#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        if r:
            for idx in range(len(r) - 1):
                print('{:d} '.format(r[idx]), end='')
            print('{:d}'.format(r[-1]))
        else:
            print('')
