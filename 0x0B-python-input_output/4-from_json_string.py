#!/usr/bin/python3
"""define from_json_string module
A function that returns an object (Python data structure)
"""
import json


def from_json_string(my_str):
    """that returns an object (Python data structure)
    represented by a JSON string

    Args:
      my_str: json represention string

    Return: python data structure
    """
    return json.loads(my_str)
