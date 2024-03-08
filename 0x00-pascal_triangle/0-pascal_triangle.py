#!/usr/bin/python3
"""
    Writing a function that produces a list of integers,
    which signifies Pascal’s triangle.
"""


def pascal_triangle(n):
    """
    Generates a list of integers that symbolize
    Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        currt = [1]
        for indx in range(len(prev) - 1):
            currt.append(prev[i] + prev[i + 1])
        currt.append(1)
        triangle.append(currt)
    return triangle
