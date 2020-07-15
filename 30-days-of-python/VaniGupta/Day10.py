#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Enter number: ")
    n = int(input())

    # inbuilt function to calculate binary 
    n = bin(n).replace("0b","")
    
    l = n.split("0")
    print(len(max(l, key = len)))
