#!/usr/bin/python3


def uppercase(str):
    for string in str:
        string = ord(string)
        if string >= 97 and string <= 123:
            string -= 32
        string = chr(string)
        print("{}".format(string), end='')
    print("")
