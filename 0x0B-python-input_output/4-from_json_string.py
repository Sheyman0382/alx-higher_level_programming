#!/usr/bin/python3
"""
    A module that defines a function which converts
    JSOn str to its python obj representaion
"""
import json


def from_json_string(my_str):
    """converts JSON string into its exact python object"""
    return json.loads(my_str)
