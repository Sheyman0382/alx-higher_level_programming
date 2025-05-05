#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        return self.my_print()

    @property
    def size(self):
        """it retrieves and returns the size
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves and returns the position
        Raises:
	    TypeErroor: if value is not a tuple of 2 integers < 0
        """

        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of this square
        Args: value of a tuple on two positive integers
	Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """computes the area the square
        Returns: the size squared
        """

        return self.__size ** 2

    def my_print(self):
        prints = ""
        if self.size == 0:
            return ("")
        for i in range(self.position[1]):
            prints += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                prints += " "
            for k in range(self.size):
                prints += "#"
            if i < self.size - 1:
                prints += "\n"
        return prints
