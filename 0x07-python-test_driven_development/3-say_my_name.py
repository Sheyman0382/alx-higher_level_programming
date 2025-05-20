#!/usr/bin/python3


"""A module that prints the user's full name"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints the full name of the user

    Args:
        first_name(str): user's first name
        last_name(str): user's last name

    Raises:
        TypeError: if first name or last name isn't a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "" and not first_name == "":
        print("My name is {}".format(first_name))
    elif first_name == "" and not last_name == "":
        print("My name is {}".format(last_name))
    elif first_name == "" and last_name == "":
        print("My name is ")
    else:
        print("My name is {} {}".format(first_name, last_name))
