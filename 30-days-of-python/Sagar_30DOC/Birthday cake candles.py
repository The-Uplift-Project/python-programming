import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    tallest=0
    count = 0
    for height in ar:
        if tallest<height:
            tallest = height
    for candles in ar:
        if tallest == candles:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
