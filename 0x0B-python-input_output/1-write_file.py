#!/usr/bin/python3
"""define write_file module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
       filename: name of the file
       text: the input text to write
    Return: number of characters
    """
    with open("{}".format(filename), "w") as filename:
        return filename.write("{}".format(text))
