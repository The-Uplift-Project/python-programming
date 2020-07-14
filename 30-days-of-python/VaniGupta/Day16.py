#!/bin/python3
import sys
print("Enter input string: ", end = "")
s = input().strip()

# simple try except to print integer 
# which are provided as string
# else print debug message
try:
    print(int(s))
except:
    print("Bad String")
