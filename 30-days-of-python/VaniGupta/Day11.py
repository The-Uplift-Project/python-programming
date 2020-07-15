#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


def calc(i,j):

    # check hourglass
    row_1 = arr[i][j]+arr[i][j+1]+arr[i][j+2]
    row_2 = arr[i+1][j+1]
    row_3 = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

    return (row_1 + row_2 + row_3)

sum = 0

for i in range(4):
    for j in range(4):
        
        s = calc(i,j)
        if s > sum: sum = s

print(sum)
