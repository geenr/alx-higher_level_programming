#!/usr/bin/python3
"""Define a function that creates an object from json file."""
import json


def load_from_json_file(filename):
    """
    Creates an object from JSON file.
    """
    with open(filename) as f:
        return (json.load(f))
