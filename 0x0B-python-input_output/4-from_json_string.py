#!/usr/bin/python3

"""
JSON encoding/decoding:
convert from json string to python object

"""

import json


def from_json_string(my_str):
    """
    Deserialize a json string

    Args:
        my_str (json): json string

    Return:
        a python object
    """

    return json.loads(my_str)
