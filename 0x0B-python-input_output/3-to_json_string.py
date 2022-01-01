#!/usr/bin/python3
"""define to_json_string module"""
import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)

    Args:
       my_obj: json represantion string
    Return: integer
    """
    return json.dumps(my_obj)
