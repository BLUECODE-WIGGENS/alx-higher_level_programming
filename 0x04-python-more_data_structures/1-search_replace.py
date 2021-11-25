#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return ([rex if rex != search else replace for rex in my_list])
