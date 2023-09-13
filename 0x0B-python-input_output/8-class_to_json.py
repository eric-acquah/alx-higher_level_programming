#!/usr/bin/python3

"""
JSON encoding/decoding
convert a class instance into json serializable dict

"""


def class_to_json(obj):
    """
    Return a dict representation of a class instance

    Args:
        obj (object): an instance of a class

    Return:
        A dict of all instance attributes
    """

    return obj.__dict__
