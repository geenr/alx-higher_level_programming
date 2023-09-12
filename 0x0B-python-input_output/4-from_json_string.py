#!/usr/bin/python3
"""Define a function that returns an object of json string."""


import json
def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str: String being tested.
    """
    return (json.loads(my_str))
