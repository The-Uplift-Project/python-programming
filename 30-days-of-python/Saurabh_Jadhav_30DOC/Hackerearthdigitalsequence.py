#Hackerearthdigitalsequence
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/digitial-sequence-ee0ea080/


n=int(input())
rc=[0]*10
recent= [False]*10
ms=0
arr=list(map(int,input().split()))
for i in range(n):
    number=arr[i]
    at=[False]*10
    #print(at)
    while(number>0):
        digit=number%10
        #print(ms)
        if not at[digit] :
            at[digit]=True
            if recent[digit] :
                rc[digit]+=1
            else:
                rc[digit]=1
                recent[digit]=True
            if rc[digit]>ms:
                ms=rc[digit]
        number=number//10
print(ms)