# Task
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2
# space-separated strings on a single line.

# Note: 0 is considered to be an even index.

print("Enter number of input values: ")
count = int(input())

for _ in range(count):
    print("Enter string to be split: ")
    inp = input()
    s1 = s2 = ""
    
    for i in range(0, len(inp), 2):
        s1 += inp[i]    
    print(s1, end = " ")
    
    for i in range(1, len(inp), 2):
        s2 += inp[i]
    print(s2)
