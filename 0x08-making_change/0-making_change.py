#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to meet a given amount.

    Args:
        coins: A list of the values of the coins in your possession.
        total: The target amount you want to reach with the coins.

    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if it's impossible.
    """
    if total == 0:
        return 0
    if total < 0:
        return -1

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
