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

    def to_json(self, attrs=None):
        """returns the dictionary description with simple
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        """
        attrs_dict = {}
        if type(attrs) == list:
            for key_item, value_item in self.__dict__.items():
                if key_item in attrs:
                    attrs_dict[key_item] = value_item
        else:
            return self.__dict__

        return attrs_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key_item, value_item in json.items():
            setattr(self, key_item, value_item)
