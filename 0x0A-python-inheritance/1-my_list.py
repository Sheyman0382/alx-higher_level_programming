#!/usr/bin/python3
"""A module that inherits from the list class"""


class Mylist(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list leaving the list unchanged"""
        print(sorted(self))
