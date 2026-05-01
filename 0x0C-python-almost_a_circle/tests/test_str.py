#!/usr/bin/python3
"""Test case module for __str__ function"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_str(unittest.TestCase):
    """Testing for the default use of __str__"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_default(self):
        """Default testing"""

        r = Rectangle(10, 3)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 10/3")

        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

        r = Rectangle(3, 5)
        self.assertEqual(str(r), "[Rectangle] ({}) 0/0 - 3/5".format(r.id))

        r = Rectangle(3, 5)
        r.width = 7
        r.height = 2
        r.x = 1
        r.y = 1
        self.assertEqual(str(r), "[Rectangle] ({}) 1/1 - 7/2".format(r.id))
