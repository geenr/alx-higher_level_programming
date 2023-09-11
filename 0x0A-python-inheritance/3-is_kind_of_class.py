#!/usr/bin/python3
"""Declaring a function that returns isinstance."""


def is_kind_of_class(obj, a_class):
    """
    Return true if object isinstance of the class or inherited.

    Args:
        obj: Object of class being tested.
        a_class: Class being tested.
    """
    return (isinstance(obj, a_class))
