#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    num1, num2 = len(matrix), len(matrix[0])
    for i in range(num1):
        for number in range(num2):
            print('{:d}'.format(matrix[num1][num2]), end="")
            if number < num2 - 1:
                print(" ", end="")
        print()
