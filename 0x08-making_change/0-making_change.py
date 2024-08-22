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
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    coins.sort(reverse=True)

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                continue
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
