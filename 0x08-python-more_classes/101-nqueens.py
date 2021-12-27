#!/usr/bin/python3

from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

user_input = argv[1]

if not isinstance(user_input, int):
    print('N must be a number')
    exit(1)

if user_input < 4:
    print("N must be at least 4")
    exit(1)
