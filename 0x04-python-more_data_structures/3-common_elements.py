#!/usr/bin/python3
def common_elements(set_1, set_2):
    same_element = set()
    for char in set_1:
        if char in set_2:
            same_element.add(char)
    return (same_element)
