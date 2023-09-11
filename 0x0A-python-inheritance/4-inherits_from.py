#!/usr/bin/python3
"""Declaring a function that returns true if object is inherited."""


def inherits_from(obj, a_class):
    """
    Return true if object is inherited.

    Args:
        obj: Inherited object being tested.
        a_class: Class being tested.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
