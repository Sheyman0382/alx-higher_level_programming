#!/usr/bin/python3
"""A BaseGeometry module"""


class BaseGeometry:
    """A base geometry class with a public method 'area()'"""
    def area(self):
        """Calculates area (to be implemented by subclasses"""
        raise Exception("area() is not implemented")
