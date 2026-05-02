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

    @property
    def size(self):
        """to define how size behaves when its called"""

        return self.width

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """a method intended to update attributes"""

        if args:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """retrns the dictionary of an instance"""

        dic = {"id": self.id, "x": self.x, "y": self.y, "size": self.size}
        return dic
