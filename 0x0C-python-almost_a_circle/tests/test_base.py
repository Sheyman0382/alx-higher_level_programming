#!/usr/bin/python3
"""A module designed to test for the Base class edge cases"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A test class to test the base class functionality/edge cases"""
    def setup(self):
        Base._Base__nb_objects = 0

    def test_default(self):
        b1 = Base()
        b2 = Base()
        """it tests if everything works fine when no id is none"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_None(self):
        """Tests when id is provided for a certain object/instance"""
        b = Base(12)
        self.assertEqual(b.id, 12)
