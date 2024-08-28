#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for keys, values in a_dictionary.items():
        if values == value:
            keys_to_del.append(keys)
    for items in keys_to_del:
        del a_dictionary[items]
    return a_dictionary
