#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    li = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        fname = firstNameEmailID[0]

        email = firstNameEmailID[1]

        if (email[-10:] == "@gmail.com"):
            li.append(fname)
    l = sorted(li)
    for i in l:
        print(i)