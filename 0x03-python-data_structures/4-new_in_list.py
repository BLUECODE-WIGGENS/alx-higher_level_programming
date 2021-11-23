#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    length = len(my_list)
    copy = my_list[:]
    if idx < 0:
        return copy
    elif idx >= length:
        return copy
    else:
        copy[idx] = element
        return copy
    return
