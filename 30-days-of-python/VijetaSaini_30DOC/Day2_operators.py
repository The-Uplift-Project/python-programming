#Day2 Code
#Operators

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=float((meal_cost/100)*tip_percent)
    tax=float((meal_cost/100)*tax_percent)
    total_cost=float(meal_cost+tip+tax)
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
