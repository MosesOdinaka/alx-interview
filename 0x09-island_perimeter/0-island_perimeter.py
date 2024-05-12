#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter of an island.
The island is represented as a 2D grid, where '0' represents water and '1'
represents land.
The grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is only one island
(or nothing).
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
    grid (List[List[int]]): A 2D list of integers representing the grid.
    '1' represents land and '0' represents water.

    Returns:
    int: The perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[-1][col] == 0:
                    perimeter += 1
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter
