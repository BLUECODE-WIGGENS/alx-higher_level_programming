#!/usr/bin/python3
"""define append_write module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
      filename: file name
      text: text to append
    Return: number of characters
    """
    with open("{}".format(filename), "a") as filename:
        return filename.write("{}".format(text))
