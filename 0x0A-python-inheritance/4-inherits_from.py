#!/usr/bin/python3
"""A module that checks if a class inherits from another class"""


def inherits_from(obj, a_class):
    """ the function checkes if 'obj' is a subclass of 'a_class'"""
    if type(obj) == a_class:
        return False
    return (issubclass(type(obj), a_class))
