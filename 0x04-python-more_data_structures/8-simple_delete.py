#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    remove_key = dict(a_dictionary)
    del remove_key[key]
    return remove_key
