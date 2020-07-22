#HackerearthSumitsloveformaths
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/sumits-love-for-maths/

#use lcm method in latter
t=int(input())
while(t>0):
    t-=1
    n,a,b,c = map(int,input().split())

    count=0
    '''
    mini=min([a,b,c])
    i=1
    while(i*a<=n):
        #print(i*a)
        i+=1
        count+=1
    i=1
    if b%a!=0:
        while(i*b<=n):
            if i%a!=0:
                count+=1
                #print(i*b)
            i+=1
    i=1
    if c%a!=0 or c%b!=0:
        while(i*c<=n):
            if i%a!=0 and i%b!=0:
                #print(i*c)
                count+=1
            i+=1
    '''
    #print(count)
    counta=n//a
    countb=n//b
    countc=n//c
    countab=n//(a*b)
    countac=n//(a*c)
    countbc=n//(b*c)
    countabc=n//(a*b*c)
    print(counta+countb+countc+countabc-countab-countbc-countac)