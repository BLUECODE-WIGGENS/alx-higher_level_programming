#!/usr/bin/python3
"""defins read_file module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open("{}".format(filename), "r") as filename:
        print(filename.read(), end="")
