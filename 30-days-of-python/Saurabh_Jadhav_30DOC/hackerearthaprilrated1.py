def dectobin(number):
    arr=[]
    while(number>0):
        arr.append(number%2)
        number=number//2
    x=16-len(arr)
    while x>0:
        arr.append(0)
        x-=1
    print(len(arr))
    arr.reverse()
    return arr
t=int(input())
while(t>0):
    t-=1
    n,m,c = input().split()
    n=int(n)
    m=int(m)
    #n,m,c=7881,5,"L"
    shift=dectobin(n)
    m=m%len(shift)
    #print(m)
    if c=="L":
        shift = shift[m:]+shift[:m]
    else:
        shift = shift[-m:]+shift[:-m]
    print(int("".join(map(str,shift)),2))
    #print(shift)
    #print(dectobin(n))
    