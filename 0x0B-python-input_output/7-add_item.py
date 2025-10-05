#!/usr/bin/python3
"""A script that adds command line arguments to a Python list
and saves them to a file as JSON.
"""
import sys
import os
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
