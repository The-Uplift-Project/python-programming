#Hackerearth Finding the Subarrays
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/counting-the-subarrays-4187713a/
n = int(input())
arr=list(map(int,input().split()))
aarr=[0]*(n+2)
for i in range(n):
    aarr[i+1]=aarr[i]+arr[i]
print(aarr)
total=aarr[-2]
#print(total)
pairs=[]
for i in range(1,n+1):
    for j in range(i,n+1):
        ra=aarr[j]-aarr[i-1]
        subrange=j-i+1
        averager=ra/subrange
        otherr = n-subrange
        if otherr>=1:
            averageo = (total-ra)/otherr
            #print(averager,averageo)
            
        else:
            averageo=0
        #print(i,j)
        
        if averager>averageo:
            print(averager,averageo)
            pairs.append([i,j])
#print(aarr)
for i in range(len(pairs)):
    #pass
    print(pairs[i][0],pairs[i][1],sep=" ")