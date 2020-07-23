#EEDC Lab
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/eedc/
#to be solved yet tle and memory limits


n=int(input())
arr=list(map(int,input().split()))
result = 0
left=[0]*(n+2)
right=[0]*(n+2)
for i in range(1,n+1):
    left[i] = 10*left[i-1] + arr[i-1]
for i in range(1,len(arr)):
    divider=10**(n-i)
    right[i] = left[-2]%divider
game=[]
#print(left)
#print(right)
queries = int(input())
for q in range(queries):
    l,r = map(int,input().split())
    pair=0
    while(l<r+1):
        grand=left[l-1]+right[l]
        if grand%2==0 and grand%3==0 and grand%5==0:
            pair+=1
            print(left[l-1],right[l],sep="\t")
        l+=1
        #grand=sumarr[j-1]+(sumarr[-1] -sumarr )
    game.append(pair)
for i in range(len(game)):
    print(game[i])
