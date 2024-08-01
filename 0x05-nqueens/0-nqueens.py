#!/usr/bin/python3
"""Recursive implementation of NQueens"""
import sys


def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This means no other queen can attack this position.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print all possible solutions.
    Each solution is printed as a list of lists,
    where each inner list contains two numbers [row, column].
    """
    def backtrack(row):
        """ Adds the solutiion to results if all queens are placed"""
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            results.append(solution)
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    board = [-1] * N
    results = []
    backtrack(0)

    for solution in results:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
