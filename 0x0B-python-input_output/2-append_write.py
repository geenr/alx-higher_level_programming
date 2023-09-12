#!/usr/bin/python3
"""Defining a function that appends a file."""


def append_write(filename="", text=""):
    """
    Appends a txt file.

    Args:
        filename: Name of the file being tested.
        text: The string being tested.
    """
    with open('file_append.txt', 'a', encoding='utf-8') as f:
        return(f.write(text))
