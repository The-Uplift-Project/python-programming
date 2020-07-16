# The function is expected to return a BOOLEAN.
# The function accepts 2D_STRING_ARRAY board as parameter.
# The function will analyze board, determine if it
# represents a valid sudoku board and returns true or
# false accordingly.

# rows: all unique numbers, blanks represented as "."
# columns: same as rows
# boxes: same as rows
# incomplete sudoku can be a valid sudoku if numbers are not repeating in row/column/boxes

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isValidSudoku' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts 2D_STRING_ARRAY board as parameter.
# The function will analyze board, determine if it
# represents a valid sudoku board and returns true or
# false accordingly.
#

def isValidSudoku(board):

    # check rows
    for i in range(len(board)):
        s = ""
        for j in range(len(board)):
            if board[i][j].isdigit():
                s += board[i][j]
        if len(s) != len(set(s)):
            return False
    # check columns
    for i in range(len(board)):
        s = ""
        for j in range(len(board)):
            if board[j][i].isdigit():
                s += board[j][i]
        if len(s) != len(set(s)):
            return False
    
    
    return True
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_rows = int(input().strip())
    board_columns = int(input().strip())

    board = []

    for _ in range(board_rows):
        board.append(input().rstrip().split())

    result = isValidSudoku(board)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
