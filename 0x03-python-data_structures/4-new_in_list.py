#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx > len(my_list):
        return (my_list.copy())
    cpy_list = my_list.copy()
    cpy_list[idx] = element
    return (cpy_list)
