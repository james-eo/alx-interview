#!/usr/bin/python3
"""Module for lockboxes implementation"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each inner
        list represents a box and contains keys (integers) to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])  # First box is always unlocked
    keys = set(boxes[0])  # Start with keys in the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(box for box in boxes[new_key] if box not in unlocked)

        if len(unlocked) == n:
            return True

    return False
