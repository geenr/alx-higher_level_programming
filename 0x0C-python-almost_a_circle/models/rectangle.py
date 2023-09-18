#!/usr/bin/python3
from models.base import Base
"""Define a class Rectangle."""


class Rectangle(Base):
    """
    Represents a class Rectangle that inherits from Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the class Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): One side of the rectangle.
            y (int): Another side of the rectangle.
            id (int): Identity of rectangle.

        Raises:
            TypeError: If width/height/x/y is not an integer.
            ValueError: If width/height/x/y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter  for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x side of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y side of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.width * self.height)

    def display(self):
        """Print the rectangle in stdout using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for a in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for b in range(self.width)]
            print("")

    def __str__(self):
        """Updates and returns the class in a string method."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the attributes of the class.

        Args:
            *args (ints): New values of the attribute.
                - 1st argument should be id attribute
                - 2nd argument should be width attribute
                - 3rd argument should be height attribute
                - 4th argument should be x attribute
                - 5th argument should be y attribute
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            f = 0
            for arg in args:
                if f == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif f == 1:
                    self.width = arg
                elif f == 2:
                    self.height = arg
                elif f == 3:
                    self.x = arg
                elif f == 4:
                    self.y = arg
                f += 1

        elif kwargs and len(kwargs) != 0:
            for i, v in kwargs.items():
                if i == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif i == "width":
                    self.width = v
                elif i == "height":
                    self.height = v
                elif i == "x":
                    self.x = v
                elif i == "y":
                    self.y = v
