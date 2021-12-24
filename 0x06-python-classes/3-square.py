#!/usr/bin/python3
"""define square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """
        Only integer on input otherwise raises an
        exception

        size: type(int)
        size: >= 0 otherwise raises exception
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        method: square area

        Return: the current square area
        """
        return self.__size * self.__size
