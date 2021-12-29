#!/usr/bin/python3
"""add_attribute module"""


def add_attrbute(object, attr, size):
    """
    Function that adds a new attribute to an object if it’s possible:
    Args:
       obj: the object add a new attribute.
       attr: attribute to add.
       size: value to set the attribute.
    Returns:
       None: nothing
    """
    if hasattr(object, "__dict__"):
        setattr(object, attr, size)
        return
    raise TypeError("can't add new attribute")
