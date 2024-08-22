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
    coins.sort(reverse=True)
    coin_count = 0

    if total <= 0:
        return 0

    for coin in coins:
        if total >= coin:
            coin_count += total // coin
            total %= coin

        if total == 0:
            return coin_count

    return -1
