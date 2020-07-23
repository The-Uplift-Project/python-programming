#Hackerearthr-Ridicules.py
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/k-rotation-is-what-you-can-855157f8/

n,d = map(int,input().split())
arr=list(map(int,input().split()))

arr=arr[d:]+arr[:d]
for i in range(n):
    print(arr[i],end=" ")