#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    Args:
       obj: object to evaluate
       a_class: class to evaluate
    Return:
        bool: True if class is class or subclass,
        otherwise False
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
