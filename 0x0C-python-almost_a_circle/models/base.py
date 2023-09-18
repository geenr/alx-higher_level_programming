#!/usr/bin/python3
"""Defining a class base."""


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
