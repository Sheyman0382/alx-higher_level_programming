#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    while count >= 0:
        print("{:d}".format(my_list[count - 1]))
        count = count - 1
