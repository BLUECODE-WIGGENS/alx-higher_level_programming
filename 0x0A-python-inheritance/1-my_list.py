#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """
        Public instance method:
        assume that all the elements
        of the list will be of type int
        """
        print(sorted(self))
