#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    result = 0
    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)
            result += element
    return result
