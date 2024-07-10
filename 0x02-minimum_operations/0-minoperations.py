#!/usr/bin/python3
"""
This module contains the function minOperations to calculate the
fewest number of operations needed to result in exactly n H characters
in the file using Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly
    n 'H' characters in a file.

    Args:
        n (int): The number of 'H' characters to be achieved.

    Returns:
        int: The minimum number of operations needed.
        Returns 0 if n is impossible to achieve.
    """
    len_h = 1
    len_compied = 0
    total_operations = 0

    while len_h < n:
        if n % len_h == 0:
            total_operations += 2
            len_copied = len_h
            len_h += len_copied
        else:
            total_operations += 1
            len_h += len_copied
    return total_operations
