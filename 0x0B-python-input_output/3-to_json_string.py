#!/usr/bin/python3
import json
"""This module defines a function tht cnverts a python obj to a JSON string"""


def to_json_string(my_obj):
    """converts a python obj to its JSON rep and return"""
    return json.dumps(my_obj)
