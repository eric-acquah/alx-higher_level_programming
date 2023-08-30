#!/usr/bin/python3

"""
This module defines a class with private attributes
"""


class Square:
    """
    This class defines a simple class with a private object attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This method initializes objects with the size varaible

        Args:
            size: constant size of square
            position: a tuple of two positive integers
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """control access to postion instance attribute"""

        return self.__position

    @position.setter
    def position(self, position):

        self.__position = position

        err_msg = "position must be a tuple of 2 positive integers"
        for item in self.__position:
            if not isinstance(item, int):
                raise TypeError(err_msg)

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
            p = self.__position[0]
            for i in range(self.__size):
                for j in range(self.__size):
                    if not self.__position[1] > 1:
                        if j == 0:
                            print(" " * p + "#", end="")
                        else:
                            print("#", end="")
                    else:
                        print("#", end="")
                print('')
