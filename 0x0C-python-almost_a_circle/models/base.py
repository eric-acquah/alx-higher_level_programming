#!/usr/bin/python3

"""
This module defines the base class for all
future classes that will be implemeted as part of the `almost circle project`

"""
import json


class Base:
    """The base class of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instances

        Args:
            id (int): id of the inheriting class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionary into json string"""
        if list_dictionaries is None:
            return f"[]"
        return json.dumps(list_dictionaries)
