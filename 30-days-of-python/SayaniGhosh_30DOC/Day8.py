# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input("Enter no of items : "))
d={}
for i in range(n):
    x = input("Enter name and no : ").split()
    d[x[0]] = x[1]
while True:
    try:
        name = input("Enter query : ")
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not found")
    except: break