#!/usr/bin/python3

"""
Create a class the inherits from the list class

"""


class MyList(list):
    """
    Class inherits from the list class

    Attribute:
        lis (list): a public list instance
    """

    def __init__(self):
        """Initialize each instance as a list"""

        self.lis = list

    def print_sorted(self):
        """sorts the int elements of the list"""

        self.clone = self.lis.copy(self)
        for i in self.clone:
            if not isinstance(i, int):
                raise TypeError("List item cannot be mixed types")
        self.clone.sort()
        print(self.clone)
