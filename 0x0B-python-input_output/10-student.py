#!/usr/bin/python3
"""A module that defines a student Class"""


class Student:
    """A class that instantiates a student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of a student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary rep of any object of  student class"""
        if isinstance(attrs, list):
            dic = {}
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return dic
        return (self.__dict__)
