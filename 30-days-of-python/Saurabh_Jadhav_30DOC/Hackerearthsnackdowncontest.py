#HackerearthSnackDownContest
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/snackdown-contest/


t= int(input())
while(t>0):
    t-=1
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    if p[0] +q[0]>= n:
        truth=[False]*n
        tr=0
        pass
        for i in range(1,len(p)):
            if not truth[p[i]-1] :
                truth[p[i]-1] =True
                tr+=1
        for i in range(1,len(q)):
            if not truth[q[i]-1] :
                truth[q[i]-1] =True
                tr+=1
        if tr==n:
            print("Yes")
        else:
            print("No")
    else:
        print("No")