t=int(input())
result=[]
while t>0:
    t-=1
    n=int(input())
    s=input()
    n=len(s)
    xa=0
    xat=0
    i=n-1
    cf=False
    while i>=0  :
        if s[i]!="B":
            cf=True
            xat=i
        if cf and s[i]=="B":
            xa+=1
        i-=1
    result.append(min(n-xa,xa))
for i in range(len(result)):
    print(result[i])

'''
2
67
AAABAABBBABBBBABBABABABBABBBBAABAAAABBAAAAABBAAAAAABBBAAAAABAAAAAAB
'''