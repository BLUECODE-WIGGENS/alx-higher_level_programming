#!/usr/bin/python3


def uniq_add(my_list=[]):
    add_unique = 0
    for unique in set(my_list):
        add_unique += unique
    return add_unique
