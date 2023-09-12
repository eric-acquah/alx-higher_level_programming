#!/usr/bin/python3

"""
Create a functon that returns a list of all available attributes
and methods of a given instance

"""


def lookup(obj):
    """
    Show all avaialable methods amd attributes

    Args:
        obj: the object

    Return:
        A list of the available attributes and methods

    """

    if not isinstance(obj, object):
        raise NameError(f"'{obj}' is not defined")
    else:
        return dir(obj)
