#!/usr/bin/python3
"""
This is the "say_my_name" module

There one function say_my_name(first_name, last_name=")
"""
def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: first string name
        last_name: second string name but has initial empty string
    Print:
        fullname: first_name + last_name
    Return:
        None: nothing to return on direct print
    Raise:
        TypeError: all inputs must be string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
