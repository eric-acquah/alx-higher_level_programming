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

    def to_json(self, attrs=None):
        """Returns a json serializable dict"""

        all_dict = self.__dict__
        dit = {}

        if isinstance(attrs, list):
            for name in attrs:
                try:
                    dit[name] = all_dict[name]
                except KeyError:
                    continue
            return dit

        return all_dict
