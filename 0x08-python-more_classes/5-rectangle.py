#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectamgle attributes
        Args:
            width: represents the width of a rectangle
            height: represents the height of a rectangle
        Raises:
            ValueError: when height or width is < 0
            TypeError: when width or height isn't an integer
        """
        self.width = width
        self.height = height

    def __str__(self):
        """nicely prints the shape of the rectangle"""
        if self.__height == 0 or self.width == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """returns a string that recreate an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an object is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """retrieves width attribute"""
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
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """computes the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
