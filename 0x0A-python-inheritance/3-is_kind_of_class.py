#!/usr/bin/python3
"""
a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Returns bool, True or False
        Args:
          obj: object ot evaluate
          a_class: a class to evaluate
        Return:
          bool: evaluates to true or false
    """
    return isinstance(obj, a_class)
