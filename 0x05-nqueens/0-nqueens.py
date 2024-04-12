#!/usr/bin/python3
"""
N-Queens Solver

Description:
Solves the N-Queens puzzle by placing N non-attacking queens on an N×N
chessboard.

Usage:
nqueens N

Arguments:
N: An integer greater than or equal to 4 (size of the chessboard).

Behavior:
- If the user provides the wrong number of arguments, it prints "Usage: nqueens
N" and exits with status 1.
- If N is not an integer, it prints "N must be a number" and exits with
status 1.
- If N is smaller than 4, it prints "N must be at least 4" and exits with
status 1.
- Prints every possible solution to the problem, one solution per line
(order not specified).

Constraints:
- Only the sys module is allowed for import.
"""

import sys


def print_solution(board):
    """
    Prints the N-Queens solution in the specified format.
    Args:
        board: A list of lists representing the chessboard.
    """
    solution = []
    for row, col in enumerate(board):
        solution.append([row, col.index(1)])
    print(solution)


def is_safe(board, row, col, N):
    """
    Checks if placing a queen at the specified position is safe.
    Args:
        board: The current state of the chessboard.
        row: The row to check.
        col: The column to check.
        N: The size of the board.
    Returns:
        True if safe, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
        if row - i >= 0 and board[row - i][col - i] == 1:
            return False
        if row + i < N and board[row + i][col - i] == 1:
            return False
    return True


def solve_NQueens_util(board, col, N):
    """
    Recursive utility function to find all solutions.
    Args:
        board: The current state of the chessboard.
        col: The current column.
        N: The size of the board.
    Returns:
        True if a solution is found, False otherwise.
    """
    if col == N:
        print_solution(board)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_NQueens_util(board, col + 1, N) or res
            board[i][col] = 0  # Backtrack
    return res


def solve_NQueens(N):
    """
    Solves the N-Queens problem and prints all solutions.
    Args:
        N: The size of the board.
    Returns:
        True if solutions exist, False otherwise.
    """
    board = [[0] * N for _ in range(N)]
    if not solve_NQueens_util(board, 0, N):
        return False
    return True


def validate_input(args):
    """
    Validates the input data.
    Args:
        args: sys.argv
    Returns:
        The size of the board (N).
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    return N


if __name__ == "__main__":
    N = validate_input(sys.argv)
    solve_NQueens(N)
