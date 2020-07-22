#Hackerearthacchedin
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/achhe-din-6baeb5d1/

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    arr = list(map(int,input().split()))
    s=set(arr)
    rouge = (sum(s)*3) - sum(arr)
    print(rouge//2)