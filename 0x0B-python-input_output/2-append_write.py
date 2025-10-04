#!/usr/bin/python3
"""A module that appends to a file"""


def append_write(filename="", text=""):
    """a function that appends to a file"""
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
