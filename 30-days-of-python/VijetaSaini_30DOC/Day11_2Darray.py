#Day11 Code
#2D array
#To print the  maximum total of values in an hour glass of format
#a b c
#  d
#e f g

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    total_values=[]

    #here len(arr)-2 is used beacuse whatever be the len of array total number or hour       #glasses vertically and horizontally will be 2 less 
    #than the len(arr) for eg. 11         
    #hourglasses will be 9


    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total_of_hourglass=0
            for row in range(i,i+3):
                for column in range(j,j+3): 
                    if(row==i or row==i+2):
                        total_of_hourglass+=arr[row][column]
                    else:
                        if(row==i+1 and column==j+1):     
                            total_of_hourglass+=arr[row][column] 
            total_values.append(total_of_hourglass)   

    #to print the maximum of all the values
    print(max(total_values))        
            
