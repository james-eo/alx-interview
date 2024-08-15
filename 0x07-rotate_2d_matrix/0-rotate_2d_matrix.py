#!/usr/bin/env python3
"""
Rotate 2D Matrix Module
This module provides a function to rotate an n x n 2D matrix
by 90 degrees clockwise.
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.
        It will be modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
