#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return ([[matrix[x][y]**2 for y in range(len(matrix[0]))]
            for x in range(len(matrix))])
