#!/usr/bin/python3
"""A method that calculates the fewest number of operations
    needed to result in exactly `n` `H` characters in the file

    Args:
        n: Length of characters
    return: An integer
"""


def minOperations(n: int) -> int:
    operation = 0
    factor = 2

    if (n < 2):
        return 0

    while (n > 1):
        while (n % factor == 0):
            operation += factor
            n //= factor
        factor += 1
    return operation
