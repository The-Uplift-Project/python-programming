'''
Given a sequence of non-negative integers, where each number is 
written in a separate line. The sequence ends with 0. Find 
how many elements of this sequence are equal to its largest element.
'''

maximum = int(input())
count = 1
a = -1
while a != 0:
  a = int(input())
  if a == maximum:
    count += 1
  elif a > maximum:
    maximum = a
    count = 1

print(count)
