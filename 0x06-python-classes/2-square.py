#!/usr/bin/python3

"""
This module defines a class with private attributes
"""


class Square:
    """
    This class defines a simple class with a private object attribute
    """

    def __init__(self, size=0):
        """
        This method initializes objects with the size varaible

        Args:
            size: constant size of square
        """

        self.__size = size

        # size must be an integer
        if type(self.__size) != int:
            raise TypeError("size must be an integer")

        # size must be 0 or geater
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
