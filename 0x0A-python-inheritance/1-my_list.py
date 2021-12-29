#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def __init__(self):
        super.__init_subclass__()

    def print_sorted(self):
        """
        Public instance method:
        assume that all the elements
        of the list will be of type int
        """
        print(sorted(self))
