#hackerearthFindTheString
#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/find-the-string-4014dec6/

from collections import Counter

t = int(input())
while t>0:
    m,n = map(int,input().split())
    mat=[]
    d={}
    for i in range(m):
        row= input()
        d[i] = Counter(row)
        mat.append(row)
    string=input()
    flag=True
    for i in range(len(string)):
        if string[i] in d[i%m]:
            
            if d[i%m][string[i]]>0:
                d[i%m][string[i]]-=1
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("No")
    
    t-=1