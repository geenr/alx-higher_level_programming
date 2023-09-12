#!/usr/bin/python3
"""Defines a function that returns the list of int of triangle."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pasc_triangle = [[1]]
    while len(pasc_triangle) != n:
        a = pasc_triangle[-1]
        b = [1]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i + 1])
        b.append(1)
        pasc_triangle.append(b)
    return pasc_triangle
