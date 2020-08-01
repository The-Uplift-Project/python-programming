# Given a positive integer, determine if it's the nth Fibonacci number for 
# some n. If it is, print such n, otherwise print -1.

n = int(input())
a = 1
b = 1
c = 0
count = 2
while c <= n:
  c = a + b
  count += 1
  
  a = b
  b = c
  
if a == n:
  print(count - 1)
else:
  print(-1)
