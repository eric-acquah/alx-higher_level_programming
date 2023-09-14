#!/usr/bin/python3

"""
This module defines a simple gemotery class

"""


class BaseGeometry:
    """Basic methods"""

    def area(self):
        """Raises an exception each time it's called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks for integer values only.

        Args:
            name (str): name of value
            value (int): integer value
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            name = value
