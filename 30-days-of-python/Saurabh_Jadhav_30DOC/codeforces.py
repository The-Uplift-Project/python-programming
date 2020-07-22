t=int(input())
while(t>0):
    t-=1
    n,x=map(int,input().split())
    arr = list(map(int,input().split()))
    #print(arr)
    
    arr = list((sorted(arr)))
    #print(arr)
    v=0
    i=0
    while(i<len(arr) and x>0):
        while(v < arr[i]-1 and x>0):
            v+=1
            x-=1
        v=arr[i]
        i+=1
    while(x>0):
        x-=1
        v+=1
    print(v)
    