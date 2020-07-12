from sys import stdin

print("Enter number of values: ")
n = int(input())
d = {}
for _ in range(n):
    val = input().split()
    d[val[0]] = val[1]

print("Enter names ot be found: ")
lst = stdin.read().splitlines()

'''
another way to take multi-line
input without knowing input line length:
try:
    while True:
        inp = raw_input()
        if inp == "":
            break
        else:
            lst.append(inp)
except EOFError:
    pass
'''

for i in range(len(lst)):
    if lst[i] in d.keys():
        print(lst[i]+"="+d[lst[i]])
    else:
        print("Not found")
