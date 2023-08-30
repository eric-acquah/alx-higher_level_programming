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

        self.size = size

    @property
    def size(self):
        """control access to size attribute"""

        return self.__size

    @size.setter
    def size(self, size):

        self.__size = size
    # size must be an integer
        if type(self.size) != int:
            raise TypeError("size must be an integer")

    # size must be 0 or geater
        elif self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates for the area of a square
        """

        return self.__size * self.__size

    def my_print(self):
        """Print a square using `#`
           Print size times
        """

        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print('')
