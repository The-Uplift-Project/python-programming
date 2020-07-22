#hackerearth
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,m,g = map(int,input().split())
t = list(map(int,input().split()))
c = list(map(int,input().split()))
c.sort()
maxi=0
jc=0
count=0
for i in range(1,len(t)):
    maxi=max(maxi,t[i]-t[i-1])
    while( jc<len(c) and c[jc]<=maxi):
        jc+=1
#print(c)
#print(t)
print(jc)