# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
d = {}
for i in range(n):
    x = input().split()#to split the string into list
    d[x[0]] = x[1]
while True:
    try:
        name = str(input())
        if name in d:
            print(name,"=",d[name],sep='')
        else : print("Not found")
    except: break
