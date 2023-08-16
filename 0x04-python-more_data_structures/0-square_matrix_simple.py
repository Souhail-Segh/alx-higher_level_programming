#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrice = []
    if matrix:
        for m in matrix:
            row = [x ** 2 for x in m]
            matrice.append(row)
        return matrice
    return matrice
