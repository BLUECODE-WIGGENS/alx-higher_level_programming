#!/usr/bin/python3
"""
    This is the "matrix_divided" module

    matrix must be a list of lists of integers or floats
        otherwise raise a TypeError exception
        'matrix must be a matrix (list of lists) of integers/floats'
    Each row of the matrix must be of the same size
        otherwise raise a TypeError exception
        'Each row of the matrix must have the same size'
    div must be a number (integer or float)
        otherwise raise a TypeError exception
        'div must be a number'
    div can’t be equal to 0
        otherwise raise a ZeroDivisionError exception
        'division by zero'
    All i of the matrix should be divided by div
        rounded to 2 decimal places

"""


def matrix_divided(matrix, div):
    """
    Args:
       matrix: list of lists of type int or float rounde to 2 decimal places
       div: integer
    Return:
        ruturns new matrix list of lists divided by div
    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for element1 in matrix:
        if not isinstance(element1, list) or len(element1) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(element1) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in element1:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(i / div, 2) for i in element1] for element1 in matrix]
