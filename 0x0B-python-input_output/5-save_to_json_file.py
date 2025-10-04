#!/usr/bin/python3
"""
    A module defines a function that writes
    an object to a text file using JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes json string into a file"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        js_file = json.dumps(my_obj)
        a_file.write(js_file)
