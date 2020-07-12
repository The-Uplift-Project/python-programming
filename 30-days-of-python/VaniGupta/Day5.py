# Hackerrank 30-days-of-code
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print("Enter number for table: ")
    n = int(input())

    for i in range(1,11):
        print(str(n) + " x " + str(i) + " = " + str(n*i))
