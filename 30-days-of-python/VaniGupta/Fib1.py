# Given a positive integer n, print the nth Fibonacci number.
# Read an integer:
n = int(input())
c = 2
a = 1
b = 1
x = 0
if n != 1:
  while c != n:
    x = a + b
    a = b
    b = x
    c += 1

if n == 1 or n == 2:
  print(1)
  
else: 
  print(x)
