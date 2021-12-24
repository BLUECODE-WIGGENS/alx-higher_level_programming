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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        method: square area

        Return: the current square area
        """
        return self.__size * self.__size
