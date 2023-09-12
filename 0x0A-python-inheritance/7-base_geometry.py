#!/usr/bin/python3
"""Initialize the BaseGeometry class."""


class BaseGeometry:
    """Represents the class BaseGeometry."""

    def area(self):
        """Not implemented/used."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validation function.

        Args:
            name: The name being tested.
            value: The value being tested.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
