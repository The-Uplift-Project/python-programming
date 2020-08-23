#Day29 Code
#Bitwise AND


#!/bin/python3

import math
import os
import random
import re
import sys

#method
def max_bitwise(n,k):
    max_bit=0
    for i in range(1,n+1):
        for j in range(1,i):
            bitwise=i&j
            if max_bit<bitwise<k:
                max_bit=bitwise
                if max_bit==k-1:
                    return max_bit
    return max_bit            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_bitwise(n,k))
