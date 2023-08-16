#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square = []
    for x in matrix:
        square = [z ** 2 for z in x]
        new_square.append(square)
    return (new_square)
