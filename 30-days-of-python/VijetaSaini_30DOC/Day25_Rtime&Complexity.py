#Day 25 Code
#Run time and complexity


import math

def isPrime(n):
    if n<=1:
        return False
    root=math.sqrt(n)
    if root.is_integer():
        return False
    for i in range(2,int(root)+1):
        if n%i==0:
            return False
    return True


no_of_inputs=int(input())
for i in range(no_of_inputs):
    n=int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
