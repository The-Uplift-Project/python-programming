'''
Given a list of numbers, swap adjacent elements in each pair 
(swap A[0] with A[1], A[2] with A[3], etc.). Print the 
resulting list. If a list has an odd number of elements, 
leave the last element intact.
'''
# Read a list of integers:
a = [int(s) for s in input().split()]
x = -1
if len(a) %2 == 1:
  x = a.pop()
for i in range(0, len(a), 2):
  a[i] , a[i+1] = a[i+1], a[i]

for i in a:
  print(i, end = " ")
if x != -1:
  print(x)
