#!/usr/bin/python3


def remove_char_at(str, n):
    i = ''
    for string in range(len(str)):
        if string != n:
            i += str(string)
    return i
