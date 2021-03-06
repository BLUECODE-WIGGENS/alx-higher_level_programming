#!/usr/bin/python3
"""Module with a script that adds all arguments to a Python list,
and then save them to a file
save_to_json_file from 5-save_to_json_file.py
load_from_json_file from 6-load_from_json_file.py
"""
import json
from sys import argv
"""imprting argv from sys"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    arg_list = load_from_json_file(filename)
except Exception:
    """raise FileaNotFoundError exception"""
    arg_list = []

for element in argv[1:]:
    """add a file to arg_list"""
    arg_list.append(element)

save_to_json_file(arg_list, filename)
