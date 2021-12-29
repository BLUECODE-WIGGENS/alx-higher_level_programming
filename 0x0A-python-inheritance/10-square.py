#!/usr/bin/python3
"""import Rectangle module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        "initializing and implementing area()"
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
