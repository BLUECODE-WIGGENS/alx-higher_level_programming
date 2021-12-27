#!/usr/bin/python3
"""define Rectangle module"""


import re


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            string += str(self.print_symbol) * self.width + '\n'
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
