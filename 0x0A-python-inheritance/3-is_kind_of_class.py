#!/usr/bin/python3

"""
    A module that checks if an object is an of a class or an
    instance of a an inheirited class
"""


def is_kind_of_class(obj, a_class):
    """A function that checks if an object is an instance of
        class or an instance of the inherited class
    """
    return (isinstance(obj, a_class))
