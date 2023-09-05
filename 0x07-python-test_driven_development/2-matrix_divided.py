#!/usr/bin/python3
"""Defining a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists.
        div (int or float): Divides all elements.

    Raises:
        TypeError: If matrix does not have alist of int/floats.
        TypeError: If div is not an int/float.
        TypeError: If each row of the matrix is not of same size.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return (new_matrix)
