#!/usr/bin/python3
"""define add_attribute module"""


def add_attrbute(object, attr, size):
    """add_attribute function"""
    if hasattr(object, "__dict__"):
        setattr(object, attr, size)
        return
    raise TypeError("can't add new attribute")
