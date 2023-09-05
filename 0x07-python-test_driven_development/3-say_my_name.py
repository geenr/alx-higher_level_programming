#!/usr/bin/python3
"""Define a function that prints first and last name."""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
