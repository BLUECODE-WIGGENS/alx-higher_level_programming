#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    check_list = []
    if n <= 0:
        return check_list
    for elements in range(1, n + 1):
        numbers = 1
        increment_list = []
        for element in range(1, elements + 1):
            increment_list += [numbers]
            numbers = numbers * (elements - element) // element
        check_list += [increment_list]

    return check_list
