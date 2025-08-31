#!/usr/bin/python3
"""A module that inherits from a rectangle class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size):
        """initializes a square"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
