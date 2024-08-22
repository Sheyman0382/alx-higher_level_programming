#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        for i in range(len(my_list) - 1):
            if my_list[0] > my_list[1]:
                temp = [my_list[0]]
            else:
                temp = [my_list[1]]
            my_list = temp + my_list[2:]
        return my_list[0]
