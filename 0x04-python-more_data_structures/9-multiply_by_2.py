#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dict = a_dictionary.copy()
    lst = list(cpy_dict.keys())
    for i in lst:
        cpy_dict[i] *= 2
    return (cpy_dict)
