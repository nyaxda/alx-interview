#!/usr/bin/python3
"""matrix rotation module"""

def rotate_2d_matrix(matrix) -> None:
    """rotates a matrix clockwise 90 degrees"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
