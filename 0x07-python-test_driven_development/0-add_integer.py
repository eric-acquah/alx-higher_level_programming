#!/usr/bin/python3

"""
This module define a simple function that adds two numbers
and return the sum

"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int/float): first operand
        b (int/float): Second operand

    Return:
        The sum of the numbers
    """

    typs = [list, dict, bool, set, str, tuple]

    for typ in typs:
        if isinstance(a, typ):
            raise TypeError("a must be an integer")
        elif isinstance(b, typ):
            raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
