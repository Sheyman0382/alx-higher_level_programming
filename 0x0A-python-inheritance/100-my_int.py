#!/usr/bin/python3
"""A module that inverts few operations of the int class"""


class MyInt(int):
    """A class that inherits from the int class"""
    def __eq__(self, other):
        """meant to invert "==" to "!=" """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """meant to invert "!=" operator to "==" """
        return int.__eq__(self, other)
