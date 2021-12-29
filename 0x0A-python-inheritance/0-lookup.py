#!/usr/bin/python3
"""
function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """Return a list object
       Args:
          obj: test object
    """
    return dir(obj)
