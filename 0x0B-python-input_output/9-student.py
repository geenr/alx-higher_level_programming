#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str): First name of the class student.
            last_name (str): Last name of the class student.
            age (int): Age of the class student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get the dictionary representation of the Student class."""
        return (self.__dict__)
