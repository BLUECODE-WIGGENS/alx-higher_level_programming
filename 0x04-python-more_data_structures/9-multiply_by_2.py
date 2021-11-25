#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dict1 = {}
    for key in list(a_dictionary.key()):
        dict1[key] = a_dictionary[key] * 2
    return dict1
