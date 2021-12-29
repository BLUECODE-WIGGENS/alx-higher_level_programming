#!/usr/bin/python3
"""
function that returns True if the object
is exactly an instance of the specified class ;
otherwise False.
"""
def is_same_class(obj, a_class):
    """return boolean
    Args:
        obj: object
        a_class: a class
    Return: bool, True or False on evaluation
    """
    return type(obj) == a_class
