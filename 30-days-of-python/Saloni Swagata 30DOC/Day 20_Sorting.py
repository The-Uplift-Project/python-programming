#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
s = 0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            s += 1
            
print(f"Array is sorted in {s} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")