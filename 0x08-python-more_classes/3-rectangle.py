#!/usr/bin/python3
"""define Rectangle module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the instance menthod itself"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width method
        Args:
           value: integer
        Raise:
            TypeError: if not int raise an exception
            ValueError: if int is < 0 raise an exception
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height method

        args:
           value: integer
        Raise:
            TypeError: if not int raise exception
            Valueerror: if int is < 0 raise exception
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter
        if width or height is equal to 0,
        perimeter is equal to 0
        """
        if self.width == 0:
            return 0
        if self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        string = ""
        if self.width == 0:
            return string
        if self.height == 0:
            return string
        for i in range(self.height):
            string += "#" * self.width + '\n'
        return string[:-1]
