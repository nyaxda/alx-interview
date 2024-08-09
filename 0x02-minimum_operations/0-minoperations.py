#!/usr/bin/python3
"""Minimum Operations module"""


def minOperations(n):
    """minimum operations to be done to result to exatcly n xters in file"""
    if (n == 0 or n == 1):
        return 0
    count = 0
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    while (n != 1):
        for i in prime_numbers:
            if n % i == 0:
                n = n // i
                count += i
                break
    return count
