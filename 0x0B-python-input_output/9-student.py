#!/usr/bin/python3

"""
Define a Student class

"""


class Student:
    """Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize an instance

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a json serializable dict"""
        return self.__dict__
