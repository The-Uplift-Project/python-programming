'''
Given a sequence of non-negative integers, where each number is 
written in a separate line. The sequence ends with 0. Print the 
number of elements of the sequence that are greater than their neighbors above.  
'''

# Read an integer:
p = int(input())
g = 0
while p != 0:
  n = int(input())
  if n > p: 
    g += 1
  p = n
print(g)
