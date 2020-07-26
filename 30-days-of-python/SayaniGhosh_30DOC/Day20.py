#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0;

for i in range(0, n):
    for j in range(0, n - 1):
        if (a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

            numberOfSwaps += 1

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
for i in range(0, n):
    if (i == 0):
        print("First Element: " + str(a[i]))

    if (i == n - 1):
        print("Last Element: " + str(a[i]))
