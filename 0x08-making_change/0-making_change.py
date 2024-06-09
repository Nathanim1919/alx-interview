#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """this function makes change for a
    given total using the least amount of coins

    Args:
        coins (List[number]): list of coins
        total (number): the total to make change for

    Returns:
        number: the least amount of coins needed to make change
    """
    if (total <= 0):
        return 0

    # Initialize dp array
    dp = [float('inf')] * (total + 1)

    # Base case: no coins needed to make change for 0
    dp[0] = 0

    # Initialize the rest of the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if (coin <= i):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                if (dp[i] == 1):
                    break

    return dp[total] if dp[total] != float('inf') else -1
