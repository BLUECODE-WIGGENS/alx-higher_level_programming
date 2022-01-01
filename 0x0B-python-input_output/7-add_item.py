#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file
save_to_json_file from 5-save_to_json_file.py
load_from_json_file from 6-load_from_json_file.py
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    arg_list = load_from_json_file(filename)
except Exception:
    arg_list = []

for element in argv[1:]:
    arg_list.append(element)

save_to_json_file(arg_list, filename)
