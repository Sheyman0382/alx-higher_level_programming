#!/usr/bin/python3
"""A base class module"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """converts json string into its python object"""

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string into a file"""

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w", encoding="utf-8") as file_1:
            if not list_objs:
                json_string = cls.to_json_string([])
            else:
                list_dictionaries = []
                for obj in list_objs:
                    list_dictionaries.append(obj.to_dictionary())
                json_string = cls.to_json_string(list_dictionaries)
            file_1.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create method"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """A class method that loads a json string from the file"""

        file_name = "{}.json".format(cls.__name__)
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as file_1:
            json_string = file_1.read()
            list_of_dict = cls.from_json_string(json_string)
            list_of_instances = []
            for dict_obj in list_of_dict:
                list_of_instances.append(cls.create(**dict_obj))
            return list_of_instances
