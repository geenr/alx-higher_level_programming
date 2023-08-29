#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Realize a square"""

    def __init__(self, size = 0):
        """Initialize a new square.

        Args:
            size (int): Size of new square.
        """

        self.size = size
    @property
    def size(self):
        """Sets current size of the square."""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Returns current area of square."""
        return (self.__size * self.__size)
