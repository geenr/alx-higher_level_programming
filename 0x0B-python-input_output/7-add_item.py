#!/usr/bin/python3
"""Script that adds all arguments to a Python list."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        filename = "add_item.json"
        add_items = load_from_json_file(filename)
    except FileNotFoundError:
        add_items = []
    add_items.extend(sys.argv[1:])
    save_to_json_file(add_items, filename)
