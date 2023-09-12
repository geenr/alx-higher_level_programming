#!/usr/bin/python3
"""Defines a class Rectangle which inherits object from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.

        Args:
            width (int): The Rectangle's width.
            height (int): The Rectangle's height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
