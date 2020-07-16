#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = meal_cost+((tip_percent/100)*meal_cost)+((tax_percent/100)*meal_cost)
    print(round(meal_cost))
if __name__ == '__main__':
    meal_cost = float(input("Enter meal cost : "))

    tip_percent = int(input("Enter tip percent : "))

    tax_percent = int(input("Enter tax percent : "))

    solve(meal_cost, tip_percent, tax_percent)
