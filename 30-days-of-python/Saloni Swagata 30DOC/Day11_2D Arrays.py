'''The size of the array is 6x6. This code finds the maximum sum of an hourglass formed by the array elements'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    i=0
    j=0
    while(i<4 and j<6):
        sum=0
        if (i<4 and j<4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if i==0 and j==0:
                s=sum
            s=max(s,sum)
        elif j==4:
            i+=1
            j=-1
        j+=1
    print(s)
