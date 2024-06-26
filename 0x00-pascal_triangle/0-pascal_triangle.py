#!/usr/bin/python3
"""This module defines the function pascal_triangle
that takes in nth integer argument.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
    list: A list of lists of integers representing Pascal's Triangle.
          Each inner list represents a row in Pascal's Triangle.
    """

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        triangle.append(row)
    return triangle
