#!/usr/bin/python3
"""
    A module that defines a function that
    creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
