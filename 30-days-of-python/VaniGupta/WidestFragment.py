'''
Given a sequence of non-negative integers, where each number is 
written in a separate line. The sequence ends with 0. Determine 
the length of the widest fragment where all the elements are 
equal to each other.
'''

prev = int(input())
curr = int(input())
c = 0
final = 0
while curr != 0:
  if prev == curr:
    c += 1
  
  if final < c:
    final = c
    
  if prev != curr:
    c = 0
  
  prev = curr
  curr = int(input())
print(final + 1)
