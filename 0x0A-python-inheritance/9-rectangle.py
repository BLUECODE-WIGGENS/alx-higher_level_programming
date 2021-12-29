#!/usr/bin/python3
"""define BaseGeometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits BaseGeometry class"""

    def __init__(self, width, height):
        """initializing Rectangle class"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calulates area of the Rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """str method
        
        Args: object itself           
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
