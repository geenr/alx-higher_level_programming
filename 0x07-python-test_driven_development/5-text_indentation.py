#!/usr/bin/python3
"""Defining a function that prints 2 new lines after a character '.' '?' and ':'."""


def text_indentation(text):
    """
    Prints 2 new line after character '.' '?' and ':'.

    Args:
        text (str): The string with the characters.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    a = 0
    while a < len(text) and text[a] == '':
        a += 1

    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in ".?:":
            if text[a] in ".?:":
                print("\n")
            a += 1
            while a < len(text) and text[a] == '':
                a += 1
            continue
        a += 1
