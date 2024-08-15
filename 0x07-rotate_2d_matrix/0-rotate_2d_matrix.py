#!/usr/bin/python3
"""
Rotate 2D Matrix module
This module contains a function that rotates a given n x n 2D matrix
90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix: The n x n 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in place; nothing is returned.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
