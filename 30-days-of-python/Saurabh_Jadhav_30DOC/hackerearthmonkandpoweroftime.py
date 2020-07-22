#Monk and Power of Time
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-power-of-time/




n=int(input())
calling = list(map(int,input().split()))
ideal = list(map(int,input().split()))
i,j=0,0
count=0
visited=[False]*len(calling)
length = len(calling)
while(j<len(ideal)):
    #print(calling,i,sep="   ")
    #print(ideal,j,sep=" ")
    if visited[i] !=True:
        count+=1
    if calling[i] == ideal[j] and visited[i] is not True:
        visited[i]=True
        j+=1
    i=(i+1)%len(calling)
    
    
    #print(end="\n\n")
print(count)