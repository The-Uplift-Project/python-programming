#!/bin/python3

import math
num=int(input())
if(num%2==0):
    if(num>=2 and num<=5):
        print("Not Weird")
    if(num>=6 and num<=20):
        print("Weird")
    if(num>20):
        print("Not Weird")
else:
    print("Weird")
