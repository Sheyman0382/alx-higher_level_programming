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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
