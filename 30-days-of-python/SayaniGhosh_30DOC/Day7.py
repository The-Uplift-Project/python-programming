#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter no of items : "))
    rev = ""
    arr = list(map(int, input("Enter items : ").rstrip().split()))
    c = len(arr) - 1
    while (c >= 0):
        rev = rev + str(arr[c]) + " "
        c = c - 1
    print(rev)


