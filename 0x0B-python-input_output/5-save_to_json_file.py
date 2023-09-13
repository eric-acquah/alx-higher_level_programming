#!/usr/bin/python3

"""
JSON encoding/decoding
serialize a python object and save it into a file

"""

import json


def save_to_json_file(my_obj, filename):
    """
    Convert serialize and save in file

    Args:
        my_obj (object): python object
        filename (str): file to save data
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
