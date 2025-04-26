#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that is tailored for a square"""

    def __init__(self, size=0):
        """Initializes the square class
        Args:
            size: the size of the square
        Raises:
            TypeError: if the value for size isn't an integer
            ValueError: if size is less that zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns: the square of the class
        """
        return self.__size ** 2
