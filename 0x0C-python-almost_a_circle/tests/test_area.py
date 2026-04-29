#!/usr/bin/python3
"""Test module for the area of rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestArea(unittest.TestCase):
    """Test cases for the area function"""

    def test_default(self):
        """Tests default cases for area"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
