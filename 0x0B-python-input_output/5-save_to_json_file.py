#!/usr/bin/python3
"""
define save_to_json_file module

a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation

    Args:
       my_obj: json representation file
       filename: The file to write json represantation
    Return: nothing
    """
    with open("{}".format(filename), "w") as filename:
        json.dump(my_obj, filename)
