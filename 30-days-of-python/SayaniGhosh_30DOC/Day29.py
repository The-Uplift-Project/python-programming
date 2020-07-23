#!/bin/python3

import math
import os
import random
import re
import sys


def bit(n, k):
    mk = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            x = i & j
            if (mk < x < k):
                mk = x
                if (mk == (k - 1)):
                    return mk
    return mk


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(bit(n, k))
