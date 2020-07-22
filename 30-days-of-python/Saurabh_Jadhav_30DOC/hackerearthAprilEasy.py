#hackerearthAprilEasy
#https://www.hackerearth.com/challenges/competitive/april-easy-20/algorithm/special-graph-2-3b2bf33c/

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    visited=[False]*(n+1)
    j=2
    for i in range(2,n):
        j=2
        while i*j <=n:
            visited[i*j]=True
            j+=1
    count=1
    print(visited)
    for i in range(2,n):
        if not visited[i]:
            count+=1
    print(n-count)
