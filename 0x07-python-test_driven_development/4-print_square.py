#!/usr/bin/python3
"""Defining a function that prints a square with character '#'."""
def print_square(size):
    """
    Prints a square with character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        [print("#", end="") for i in range(size)]
        print("")
