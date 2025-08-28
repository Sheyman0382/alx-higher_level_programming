#!/usr/bin/python3
"""A BaseGeometry Module"""


class BaseGeometry:
    """A base geometry class with area and integer validator public methids"""
    def area(self):
        """Calculates area (implemented by subclasses)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is an integer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
