# Day 5 Hackerrank Coding Challenge
# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def print_table(n):
    for i in range(1,10):
        print(str(n) + " x " + str(i) + " = " + str(n*i))
    print(str(n) + " x " + "10" + " = " + str(n*10))

if __name__ == '__main__':
    n = int(input())
    print_table(n)
