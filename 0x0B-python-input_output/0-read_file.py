#!/usr/bin/python3
"""Declaring a function that reads a txt file."""


def read_file(filename=""):
    """
    Reads a txt file.
    """
    with open('my_file_0.txt',  encoding='utf-8') as g:
        print(g.read(), end='')
