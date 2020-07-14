# Itertool library in Python
# Hackerrank : https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]

for i in list(product(A,B)):
    print(i, end=' ')
