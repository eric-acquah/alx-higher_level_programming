#!/usr/bin/python3

"""
This module defines a class with private attributes
"""


class Square:
    """
    This class defines a simple class with a private object attribute
    """

    def __init__(self, size=None):
        """
        This method initializes objects with the size varaible

        Args:
            size: constant size of square
        """

        self.__size = size
