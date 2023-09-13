#!/usr/bin/python3

"""
JSON encoding/decoding:
convert object to string

"""

import json


def to_json_string(my_obj):
    """
    Convert an object to json string

    Args:
        my_obj (str): object to be converted

    Return:
        json string representation the object
    """
    return json.dumps(my_obj)
