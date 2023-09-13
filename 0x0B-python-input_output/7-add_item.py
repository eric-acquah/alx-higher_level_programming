#!/usr/bin/python3

"""
A script to add commandline args to a list
and save it into a file in json format

"""

import json
import sys
json_save = __import__("5-save_to_json_file").save_to_json_file
json_load = __import__("6-load_from_json_file").load_from_json_file

argv_list = []

for args in range(1, len(sys.argv)):
    argv_list.append(sys.argv[args])

json_save(argv_list, "add_item.json")

argv_list = json_load("add_item.json")

print(argv_list)
