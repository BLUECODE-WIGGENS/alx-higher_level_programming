#!/usr/bin/python3
"""
define class_to_json module
a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """a function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
       obj: dictionary(object)
    Return:
        dict: description with simple data structure
    """
    return obj.__dict__