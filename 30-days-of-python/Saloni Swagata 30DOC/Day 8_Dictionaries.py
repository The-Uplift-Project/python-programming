# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input("Enter the number of contacts: "))
d={}
while(T>0):
    T-=1
    name, number=input("Enter the name and number: ").split()
    d[name]=number
while(True):
    try:
        x=input("Enter the name to be searched: ")
        if x in d:
            print(f"{x}={d[x]}")
        else:
            print("Not found")
    except:
        break
