#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
    coins (list of int): A list of coin denominations available.
    total (int): The total amount to reach with the fewest coins.

    Returns:
    int: The fewest number of coins needed to meet `total`,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
