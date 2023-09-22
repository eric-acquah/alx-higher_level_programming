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
        """
        converts a list of dictionary into json string

        Args:
            list_dictionaries (list): list of dictionaries to be converted

        Return:
            string representaion of the list of dictionaries
        """

        if list_dictionaries is None:
            return f"[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the string representation of an instance into a file

        Args:
            list_objs (object): instance to serialize
        """

        with open(f"{list_objs[0].__class__.__name__}.json", 'w') as f:

            obj_list = []  # list to store a dictionary of instance attributes

            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
                return

            for li in list_objs:
                obj_list.append(li.to_dictionary())
            f.write(cls.to_json_string(obj_list))
