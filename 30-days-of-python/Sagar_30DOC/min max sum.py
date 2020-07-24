import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    mini = sum(arr)-max(arr)
    maxi = sum(arr)-min(arr)
    print(mini , maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
