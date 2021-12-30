#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    Args:
      filename: the name of the file to read from
    """
    with open("".format(filename), "r") as filename:
      print(filename.read(), end="")
