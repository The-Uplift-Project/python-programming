#HACKEREARTHsumitaandequalarray
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/sumit-and-equal-array/

t=int(input())
while(t>0):
    t-=1
    n,x,y,z = map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(n):
        num=arr[i]
        flag=False
        while(num>0 or flag==False):
            pass