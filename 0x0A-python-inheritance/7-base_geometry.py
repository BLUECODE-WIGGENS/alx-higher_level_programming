#!/usr/bin/python3
"""define BaseGeometry module"""


class BaseGeometry:
    """BasaGeometry class"""
    def area(self):
        """area method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: validates value
           Return: nothing
           Raises:
                TypeError: if not int raise exception
                ValueError: if value <= 0 raise exception
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
