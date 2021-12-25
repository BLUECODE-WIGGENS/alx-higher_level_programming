#!/usr/bin/python3
"""
This is the "print_square" module

There is one function print_square(size)
"""


def print_square(size):
    """
    Args:
       size: integer
    Raise:
        TypeError: if type is not int
        ValueError: if values is < 0
    Print:
        character: a square with #, for example
    print_square(4)
    >>>####
       ####
       ####
       ####
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float:
        raise TypeError("size must be an integer")

    for elements in range(size):
        print("#" * size)
