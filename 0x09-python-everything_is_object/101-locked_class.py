#!/usr/bin/python3

"""A module that restricts unwanted attribute"""


class LockedClass:
    """A class whose objects only allow a specific attributes"""


    __slots__ = ["first_name"]
