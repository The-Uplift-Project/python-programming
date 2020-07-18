#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    print(round(meal_cost + tip + tax))

if __name__ == '__main__':
    print("Enter cost of meal: ")
    meal_cost = float(input())

    print("Enter tip percentage: ")
    tip_percent = int(input())

    print("Enter tax_percentage: ")
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
