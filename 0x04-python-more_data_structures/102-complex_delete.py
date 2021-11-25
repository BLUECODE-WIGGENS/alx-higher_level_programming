#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    erase_key = []
    for key_value, v in a_dictionary.items():
        if a_dictionary[key_value] == value:
            erase_key.append(key_value)
    for key in erase_key:
        a_dictionary.pop(key)
    return a_dictionary
