#!/usr/bin/python3
"""A base class module"""
import json


class Base:
    """The base class for every other classes that will be created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """a function that instantiate an id for every object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a python object to a json string"""

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)           
