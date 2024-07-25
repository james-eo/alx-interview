#!/usr/bin/python3
"""This module contains a function that impplements utf-8 validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the byte sequence.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    i = 0
    while i < len(data):
        if data[i] & 0x80 == 0x00:
            i += 1
        elif data[i] & 0xE0 == 0xC0:
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif data[i] & 0xF0 == 0xE0:
            if i + 2 >= len(data) or data[i + 1] & 0xC0 != 0x80 or data[i + 2]\
                    & 0xC0 != 0x80:
                return False
            i += 3
        elif data[i] & 0xF8 == 0xF0:
            if i + 3 >= len(data) or data[i + 1] & 0xC0 != 0x80 or data[i + 2]\
                    & 0xC0 != 0x80 or data[i + 3] & 0xC0 != 0x80:
                return False
            i += 4
        else:
            return False
    return True
