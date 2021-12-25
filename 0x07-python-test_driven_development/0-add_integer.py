#!/usr/bin/python3
"""
This is the "add_integer" module

This module adds two integers and return its sum in type int
This module has one function, add_integer(). 

>>>add_integer(5, 8)
13
"""
def add_integer(a, b=98):
    """
    Args:
        a: number to add
        b: another number to be added
    
    Returns:
          integer: even if the input is float number or int type
    Raises:
          TypeError: a must be an integer or b must be an integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
        
    return int(a + b)
