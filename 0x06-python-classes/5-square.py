#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes the class attributes
        Args:
            size: the size of a square
        Raises:
            TypeError: if size isn't an integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
    """
        calculates the area of square
        Returns: the area of sqaure calculated
    """
        return self.__size **2

    def my_print(self):
    """Prints the shape of square basw on the size of square"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
