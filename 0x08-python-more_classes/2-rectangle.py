#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing the rectangle attributes
        Args:
            width: represent the width of a rectangle object
            height: represents the height of a rectangle
        Raises:
            TypeError: when width or height isn't an integer
            ValueError: when width or height is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """computes the perimeter of a rectangle"""
        if width == 0 or height == 0:
            return 0
        return 2 * (self.__width + self.__height)
