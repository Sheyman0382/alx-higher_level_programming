#!/usr/bin/python3
"""unittest module for the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the functionality/edge cases for rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_default_ids(self):
        """defaut condition of the rectangle class"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_type_errors(self):
        """checking if the rectangle class catches type_error"""

        with self.assertRaises(TypeError):
            Rectangle("verify", 2)

        with self.assertRaises(TypeError):
            Rectangle(22, "32")

    def test_value_error(self):
        """checks if rectangle class catches value_errors"""

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(22, -2)
