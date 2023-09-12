#!/usr/bin/python3
"""Declaring a function that reads a txt file."""


def read_file(filename=""):
    """
    Reads a txt file.

    Args:
        filename: The txt file being read.
    """
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        print(f.read(), end='')
