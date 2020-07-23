#Roy and Symmetric Logos
#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/roy-and-symmetric-logos-1/

from math import ceil
t=int(input())
result=[]
while(t>0):
    t-=1
    n=int(input())
    mat=[]
    for i in range(n):
        rows=input()
        mat.append(rows)
    #rows
    m=n=len(mat)-1
    #col
    middle = ceil(n/2)
    flag=True
    for i in range(middle):
        for j in range(middle):
            if mat[i][j] != mat[i][m-j] or mat[i][j] != mat[m-i][n-j] or mat[i][j] != mat[m-i][j]:              
                flag=False
                break
        if flag==False:
            break
    #middle row check
    if flag and n%2==0:
        for i in range(n):
            print(mat[middle][i],mat[i][middle])
            if mat[middle][i]!=mat[middle][n-i]:
                flag=False
                break
            if mat[i][middle]!=mat[n-i][middle]:
                flag=False
                break
    if flag:
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)