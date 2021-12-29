#!/usr/bin/python3
"""define MyInt module"""

class MyInt(int):
    """MyInt class"""

    def __eq__(self, number):
        """
        Args:
           self: the object itself
           number: int object to compare
        Return:
           bool: True or False
        """
        if int(self) == int(number):
            return False
        else:
            return True

    def __ne__(self, number):
        """
        Args:
           self: the object itself
           number: int object to compare
        Return:
           bool: True or False
        """
        if int(self) != int(number):
            return False
        else:
            return True
