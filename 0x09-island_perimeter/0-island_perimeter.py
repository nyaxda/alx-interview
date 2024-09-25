#!/usr/bin/python3
"""Perimeter Module"""


def space_determiner(grid, i, j):
    """Determines the perimeter of a space"""
    perimeter = 0
    if grid[i][j] == 1:
        if i == 0 or grid[i - 1][j] == 0:
            perimeter += 1
        if i == len(grid) - 1 or grid[i + 1][j] == 0:
            perimeter += 1
        if j == 0 or grid[i][j - 1] == 0:
            perimeter += 1
        if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
            perimeter += 1
    return perimeter


def island_perimeter(grid):
    """Determines total perimeter of an island"""
    total_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total_perimeter += space_determiner(grid, i, j)
    return total_perimeter
