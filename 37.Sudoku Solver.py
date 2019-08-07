'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''

#=====================================================================================================#

# First


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return

        A = set('123456789')
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        block = [[set() for i in range(3)] for i in range(3)]
        unfilled = []

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    unfilled.append((i, j))
                else:
                    row[i].add(c)
                    col[j].add(c)
                    block[i//3][j//3].add(c)

        def solve(board, unfilled, row, col, block):
            if len(unfilled) == 0:
                return True
            i, j = min(unfilled, key=ret_len)
            option = A-(row[i] | col[j] | block[i//3][j//3])
            if len(option) == 0:
                return False
            unfilled.remove((i, j))
            for c in option:
                board[i][j] = c
                row[i].add(c)
                col[j].add(c)
                block[i//3][j//3].add(c)
                if solve(board, unfilled, row, col, block):
                    return True
                else:
                    board[i][j] = '.'
                    row[i].remove(c)
                    col[j].remove(c)
                    block[i//3][j//3].remove(c)
            unfilled.append((i, j))
            return False

        def ret_len(args):
            i, j = args
            option = A-(row[i] | col[j] | block[i//3][j//3])
            return len(option)

        solve(board, unfilled, row, col, block)
# 48ms, 13.4MB
#

#=====================================================================================================#
