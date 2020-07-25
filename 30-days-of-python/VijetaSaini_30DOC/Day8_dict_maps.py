#Day8 Code
#Dictionaries and Maps


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n =int(input())
data={}
for i in range(n):
    x = input().split()
    data[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in data:
            print(name, "=", data[name],sep="")
        else:
             print("Not found")
    except:
         break
