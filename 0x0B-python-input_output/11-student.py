#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            item = {}
            for i in attrs:
                if hasattr(self, i):
                    item[i] = getattr(self, i)
            return item

        return self.__dict__
            
    def reload_from_json(self, json):
        """A function that in real sense updates the __dict__ of the instance that called it"""
        for keys,values in json.items():
             setattr(self, keys,values)
