#!/usr/bin/python3
"""Define a Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a class square that inherits from rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the class Square.

        Args:
            size (int): The size of the square.
            x (int): One side of the square.
            y (int): The other side of the square.
            id (int): The identification of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes..

        Args:
            *args (ints): New attribute values.
                - 1st argument should be id attribute
                - 2nd argument should be size attribute
                - 3rd argument should be x attribute
                - 4th argument should be y attribute
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            f = 0
            for arg in args:
                if f == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif f == 1:
                    self.size = arg
                elif f == 2:
                    self.x = arg
                elif f == 3:
                    self.y = arg
                f += 1

        elif kwargs and len(kwargs) != 0:
            for i, v in kwargs.items():
                if i == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif i == "size":
                    self.size = v
                elif i == "x":
                    self.x = v
                elif i == "y":
                    self.y = v

    def __str__(self):
        """Updates the string format of the sqaure."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, 
            self.width))

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
