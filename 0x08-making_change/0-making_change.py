#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    count = 0
    while len(coins):
        max_currency = max(coins)
        while total >= max_currency:
            total -= max_currency
            count += 1
            if total == 0:
                break
        coins.remove(max_currency)
    if total > 0:
        return -1
    return count
