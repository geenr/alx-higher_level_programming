#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_y = 0
    for x in set(my_list):
        add_y += x
    return (add_y)
