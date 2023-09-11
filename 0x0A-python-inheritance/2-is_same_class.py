#!/usr/bin/python3
"""Declaring a function that returns true if object is an instance of class."""


def is_same_class(obj, a_class):
    """
    Returns true if object belongs to a class.

    Args:
        a_class: Class being tested.
        obj: Object being tested.
    """
    return (type(obj) == a_class)
