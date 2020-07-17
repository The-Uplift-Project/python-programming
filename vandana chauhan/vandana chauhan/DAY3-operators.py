#!/bin/python3

import math
mealCost=float(input())
tipPercent=int(input())
taxPercent=int(input())
tip=mealCost*(tipPercent/100)
tax=mealCost*(taxPercent/100)
totalcost=mealCost+tip+tax
print(round(totalcost))
