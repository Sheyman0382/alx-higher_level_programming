#!/usr/bin/python3

"""Addition module"""


def add_integer(a, b=98):
    """adds two integers together
    raise: TypeError(if a or b isn't an integer or a float)
    return: the sum of two numbers
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int (a) + int (b)
