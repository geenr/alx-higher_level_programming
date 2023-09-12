#!/usr/bin/python3
"""Define a function to return json."""


import json
def to_json_string(my_obj):
    """
    Returns an object represented by a json string.

    Args:
        my_obj: The string being tested.
    """
    return (json.dumps(my_obj))
