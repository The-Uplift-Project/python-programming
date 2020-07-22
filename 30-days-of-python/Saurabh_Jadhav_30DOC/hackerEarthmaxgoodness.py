#HackerearthMaximumGoodness
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximum-goodness/

n=int(input())
arr = list(map(int,input().split()))
currmax=0
m=0
co=0
cz=0
index=1
startindex=0
currstartindex=0
end=0
for i in range(n):
    if arr[i] == 1:
        co+=1
    else:
        cz+=1
    diff=abs(co-cz)
    currmax=diff
    if currmax==0:
        currstartindex=i
    r=end-currstartindex
    if currmax>=m :
        m=currmax
        end=i
        if r>index-startindex:
            index=i
            startindex=currstartindex
    #print(currmax)
print(index+1-startindex)