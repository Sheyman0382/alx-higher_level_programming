#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestDisplay(unittest.TestCase):

    def test_display_2x3(self):
        r = Rectangle(2, 3)

        captured = StringIO()
        sys.stdout = captured

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), "##\n##\n##\n")
