#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter the length of the array: "))

    arr = list(map(int, input("Enter the array elements: ").rstrip().split()))
    arr=arr[::-1]
    for i in arr:
        print(i, end=" ")
