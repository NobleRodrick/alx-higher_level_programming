#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function finds the square of integers of a matrix"""
    squares_matrix = matrix.copy()

    for i in range(len(matrix)):
        squares_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (squares_matrix)
