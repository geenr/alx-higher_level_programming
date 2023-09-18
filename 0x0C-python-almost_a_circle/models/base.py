#!/usr/bin/python3
"""Defining a class base."""
import json


class Base:
    """
    Representing a class Base.

    Private class attribute:
        __nb_objects (int): Number of objects in the class.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Intialize the class Base.

        Args:
            id: The class identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
