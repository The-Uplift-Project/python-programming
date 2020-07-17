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

    allsums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            val = 0
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row == i or row == i + 2:
                        val += arr[row][col]
                    elif row == i + 1 and col == j + 1:
                        val += arr[row][col]
            allsums.append(val)
    print(max(allsums))