#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """
    This represents a rectangle.
    
    Attributes:
    number_of_instances (int): The number of rectangle instances.
    print_symbol (any): This is used as a symbol of string representation.
    """
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """
        Initialize a new instance in the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets thw width of the rectangle."""
        return self.__width
        
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The value of the new width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height
        
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The value of the new height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """Gets the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Gets the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
        
    def __str__(self):
        """Returns a string representation of the rectangle using '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""

        empt = []
        for i in range(self.__height):
            [empt.append('#') for c in range(self.width)]
            if i != self.__height - 1:
                empt.append("\n")
        return ("".join(empt))
        
    def __repr__(self):
        """Returns a string representation of the rectangle to be able to recreate it."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
        
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on their areas.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This returns a new Rectangular instance with width height and size equal.

        Args:
            size (int): The size of the square.
        """
        return (cls(size, size))
