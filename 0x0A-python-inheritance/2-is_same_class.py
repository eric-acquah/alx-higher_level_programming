#!/usr/bin/python3

"""
Validate if an object is an instance of a given class

"""


def is_same_class(obj, a_class):
    """
    Checks for relationship between an object and a class

    Args:
        obj (object): the object
        a_class (class): the given class

    Return:
        True, if `obj` is instance of `a_class` else false
    """

    return True if type(obj) is a_class else False
