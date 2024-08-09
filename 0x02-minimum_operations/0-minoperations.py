#!/usr/bin/python3
"""Minimum Operations module"""


def minOperations(n):
    """minimum operations to be done to result to exatcly n xters in file"""
    if (n <= 1):
        return 0
    count = 0
    factor = 2
    while (n > 1):
        while n % factor == 0:
            count += factor
            n //= factor
        factor += 1
    return count
