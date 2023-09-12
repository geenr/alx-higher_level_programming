#!/usr/bin/python3
"""Define a function that writes a file."""


def write_file(filename="", text=""):
    """
    Writes a string to a txt file.

    Args:
        filename: The name of the file being tested.
        text: The string being written.
    """
    with open('my_first_file.txt', 'w', encoding='utf-8') as w:
        return (w.write(text))
