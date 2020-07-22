import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    l = 0
    r = 0
    for i in range(len(arr)):
        l = l + arr[i][i]
        r = r + arr[i][n-1-i]
    return abs(l-r)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
