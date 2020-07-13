#!/bin/python3

import math
import os
import random
import re
import sys


def getbinary(n):
    b=0
    s=0
    t=0
    while n>0:
        d=n%2
        if d==1:
            s+=1
            if s>=t:
                t=s
        else:
            s=0
        n=n//2
    return t


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    b = getbinary(n)
    print(b)
