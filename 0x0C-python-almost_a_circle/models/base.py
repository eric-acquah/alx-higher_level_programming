#!/usr/bin/python3

"""
This module defines the base class for all
future classes that will be implemeted as part of the `almost circle project`

"""

import json
import importlib


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
            string representaion of the list of dictionaries if successful
            else return an empty list
        """

        if list_dictionaries is None:
            empty_obj = []
            return json.dumps(empty_obj)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the string representation of an instance into a file

        Args:
            list_objs (object): instance to serialize
        """

        with open(f"{cls.__name__}.json", 'w') as f:

            obj_list = []  # list to store a dictionary of instance attributes

            if list_objs is None or list_objs == []:
                f.write(cls.to_json_string(obj_list))
                return

            for li in list_objs:
                obj_list.append(li.to_dictionary())
            f.write(cls.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Create an and set the attributes of an instance

        Args:
            dictionary (dict): dictionary of attributes
            to be passed to the new instance

        Return:
            The newly created an set instance
        """
        if cls.__name__ == "Square":
            # import only when it's needed to avoid circular dependancies
            Square = importlib.import_module("models.square").Square

            cls.dummy = Square(1)  # crearte a dummy instance

            cls.dummy.update(**dictionary)  # use upadte method of child class
            # to update the new instance with the actual values

            return cls.dummy

        else:

            Rectangle = importlib.import_module("models.rectangle").Rectangle

            cls.dummy = Rectangle(1, 3)

            cls.dummy.update(**dictionary)

            return cls.dummy

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list of dictionary represented in json string

        Args:
            json_string (str): list of json strings

        Return:
            the list of json strings if json_string is not None
            else return an empty list
        """
        if json_string is None:
            return json.loads(Base.to_json_string([]))
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        try:
            cls.obj_list = []
            # File name must be name_of_class.json
            with open(f"{cls.__name__}.json", 'r') as f:

                # this method returns a list of json strings read from the file
                read_list = cls.from_json_string(f.read())

                for attr_dict in read_list:  # Extract each dict in the list

                    # for each dict, create a new instance of the given class
                    # and append to a list of instances
                    cls.obj_list.append(cls.create(**attr_dict))

                return cls.obj_list

        except FileNotFoundError:
            # Return an empty list if file was not found
            return cls.obj_list
