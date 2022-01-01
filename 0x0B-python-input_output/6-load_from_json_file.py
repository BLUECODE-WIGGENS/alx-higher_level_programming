#!/usr/bin/python3
"""
function that creates an Object from a “JSON file
Define load_from_file module
"""
import json


def load_from_file(filename):
    with open(filename) as filename:
        """
        function that creates an Object from a “JSON file

        Args:
           filename: file to load json representation from
        
        Return: nothing
        """
        json.load(filename)
