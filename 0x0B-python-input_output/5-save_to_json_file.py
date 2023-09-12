#!/usr/bin/python3
"""Define a function that writes an object to a text file."""


import json
def save_to_json_file(my_obj, filename):
    """
    Writes a object to a text file using JSON.

    Args:
        my_obj: Object being written.
        filename: The name of the file being tested.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
