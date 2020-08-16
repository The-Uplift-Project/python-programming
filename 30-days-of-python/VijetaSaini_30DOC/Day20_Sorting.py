#Day20 Code
#Sorting

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totalswaps=0

for i in range(len(a)-1,0,-1):
    numberofswaps=0
    for j in range(i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numberofswaps+=1
    totalswaps+=numberofswaps
                
    if numberofswaps==0:
        break

print("Array is sorted in {} swaps.".format(totalswaps)) 
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))               
