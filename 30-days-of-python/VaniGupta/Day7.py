#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Enter number of elements: )
    n = int(input())
    print("Enter elements: ")
    arr = list(map(int, input().rstrip().split()))
    x = reversed(arr)
    print(*x)
    
    # another method is using list comprehension
    # return(arr[::-1]
