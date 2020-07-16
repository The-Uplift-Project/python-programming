#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# keeping count of number of swaps
s = 0

# bubble sort to sort input list in ascending order
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            s += 1
            
# printing the required outputs
print("Array is sorted in {} swaps.".format(s))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
