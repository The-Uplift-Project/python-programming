#Day6 Code
#Lets's_review


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(0,n):
    name=str(input())
    print(name[::2], name[1::2])
