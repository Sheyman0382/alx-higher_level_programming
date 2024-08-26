#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    temp_keys, temp_values = "", 0
    for keys, values in a_dictionary.items():
        if temp_values < values:
            temp_keys, temp_values = keys, values
    return temp_keys
