#!/usr/bin/python3
def element_in_index(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        return (my_list[idx])
