#Dedication Level = Infinity
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/baaki-che/

n=int(input())
arr=[]
for i in range(n):
    pair=list(map(str,input().split()))
    pair[1]=int(pair[1])
    arr.append(pair)
topt=sorted(arr,key=lambda pair:pair[1])
for i in range(-1,-4,-1):
    print(topt[i][0])
