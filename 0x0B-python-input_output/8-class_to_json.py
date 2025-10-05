#!/usr/bin/python3
"""Module that returns a dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary representation of an object
    suitable for JSON serialization.
    """
    return obj.__dict__
