#!/usr/bin/python3
"""Define a function that returns the sum of two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int (a) + int (b))
