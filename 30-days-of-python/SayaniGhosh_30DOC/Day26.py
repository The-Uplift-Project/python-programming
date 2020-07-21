# Enter your code here. Read input from STDIN. Print output to STDOUT
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))

if(li2[2]<li1[2]):
    a=li1[2]-li2[2]
elif(li2[2]==li1[2]):
    a=0
else:
    a=-1

if(a==0):
    if(li2[1]<li1[1]):
        b=li1[1]-li2[1]
    else:
        b=0

    if(li2[0]<li1[0]):
        c=li1[0]-li2[0]
    else:
        c=0


if(a==-1):
    print(0)
elif(a==0)and(b!=0):
    print(500*b)
elif(a==0)and(b==0):
    print(c*15)
elif(a!=0)and(a!=-1):
    print(10000)
