#!/usr/bin/python3
"""A module that defines a student Class"""


class Student:
    """A class that instantiates a student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of a student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary rep of any object of  student class"""
        return (self.__dict__)
