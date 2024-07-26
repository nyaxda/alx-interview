#!/usr/bin/python3
"""
Pascals Triangle
"""
import math


def binomial(n, k):
    return math.comb(n, k)


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [binomial(i, j) for j in range(i + 1)]
        triangle.append(row)
    return triangle
