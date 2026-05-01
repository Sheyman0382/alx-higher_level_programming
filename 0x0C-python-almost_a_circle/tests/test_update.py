#!/usr/bin/python3
"""Test module for the update method"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestUpdateMethod(unittest.TestCase):
    """To check if attributes are truly updated"""

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10, 10)

    def test_id_update(self):
        """to test if the id was updated successfully"""

        self.r.update(89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 10/10")

    def test_width_update(self):
        """test if the width was updated successfully"""

        self.r.update(89, 2)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/10")

    def test_height_update(self):
        """test if height was updated successfully"""

        self.r.update(89, 2, 3)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/3")

    def test_x_update(self):
        """test if x was updated successfully"""

        self.r.update(89, 2, 3, 4)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/10 - 2/3")

    def test_y_update(self):
        """test if y was updated successfully"""

        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")
