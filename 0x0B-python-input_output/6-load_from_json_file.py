#!/usr/bin/python3

"""
JSON encoding/decoding:
Deserialize from a file

"""

import json


def load_from_json_file(filename):
    """
    Deserialize from a file

    Args:
        filename (str): file to load from

    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
