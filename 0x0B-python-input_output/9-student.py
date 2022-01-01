#!/usr/bin/python3
"""
define Student class module
"""


class Student:
    """
    Student class
    public instances attributes:
        first_name: student's first name
        last_name: student's last name
        age: student's age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        """
        return self.__dict__
