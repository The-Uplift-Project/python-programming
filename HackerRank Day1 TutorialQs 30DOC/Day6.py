# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input("Enter test cases : "))
for j in range(0, t):
    st = input("Enter string : ")
    c=0
    odd=""
    even=""
    for i in st:
        if((i!=" ") and (c%2==0)):
            odd=odd+i
        if((i!=" ") and (c%2!=0)):
            even=even+i
        c=c+1
    print(odd+" "+even)