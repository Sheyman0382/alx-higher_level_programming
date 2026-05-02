#!/usr/bin/python3
"""A module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """the square class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation for the square class"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
