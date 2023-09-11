#!/usr/bin/python3
"""Initialize a class MyList."""


class MyList(list):
    def print_sorted(self):
        """
        Prints a sorted list.
        """
        sort_list = sorted(self)
        print(sort_list)
