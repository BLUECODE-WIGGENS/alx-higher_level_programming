#!/usr/bin/python3
"""define module"""

class LockedClass:
    """prevents the user from dynamically
       creating new instance
    """
    __slots__ = ['first_name']
