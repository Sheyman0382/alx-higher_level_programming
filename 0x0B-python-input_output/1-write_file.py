#!/usr/bin/python3
"""A module that writes into a file"""


def write_file(filename="", text=""):
    """a function that writes into a file"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
