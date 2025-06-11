#!/usr/bin/python3
"""A module that creates a rectangle class"""


class Rectangle:
    """Blueprint for a rectangle class"""

    def __init__(self, width=0, height=0):

        """A function that initializes a rectangle class
        Args:
            width: the rectangle width
            height: height of the rectangle
        Raises:
            ValueError: when width or height is negative
            TypeError: when width or height is not an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @setter.width
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @setter.height
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
