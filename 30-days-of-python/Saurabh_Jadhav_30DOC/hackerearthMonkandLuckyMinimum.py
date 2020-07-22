#hackerearthMonkandLuckyMinimum
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-lucky-minimum-3/
INT_MAX=10**9

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    nd={}
    min_freq=0
    min_e=INT_MAX+1
    for i in range(len(arr)):
        if arr[i]<min_e:
            min_e = arr[i]
            min_freq=1
        elif arr[i] == min_e:
            min_freq+=1
    if min_freq %2 !=0:
        print("Lucky")
    else:
        print("Unlucky")