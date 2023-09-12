#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student class.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(j) == str for j in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The value pairs to replace attributes with.
        """
        for m, i in json.items():
            setattr(self, m, i)
