#!/usr/bin/python3
"""This module defines a function tht cnverts a python obj to a JSON string"""
import json


def to_json_string(my_obj):
    """converts a python obj to its JSON rep and return"""
    return json.dumps(my_obj)
