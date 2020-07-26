#HackerearthCanYouSolveIt?
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/

'''
Interesting approach
abs(a[i]-a[j])+abs(i-j)
means that this has 2 cases
case1:  a[i]+i max and a[j]+j min
case2: a[j]+j max and a[i]+i min

'''
INT_MAX=(10**5)+1
INT_MIN=-(10**5)-1
t=int(input())
while(t>0):
    t-=1
    
    n=int(input())
    arr=list(map(int,input().split()))
    max1,max2,min1,min2 = INT_MIN,INT_MIN,INT_MAX,INT_MAX
    for i in range(n):
        if max1< arr[i]+i:
            max1=arr[i]+i
        if min1 > arr[i]+i:
            min1 = arr[i]+i
        if max2 < arr[i]-i:
            max2 = arr[i]-i
        if min2 > arr[i]-i:
            min2 = arr[i]-i
    #print(max1,max2,min1,min2)
    print(max(max1-min1,max2-min2))