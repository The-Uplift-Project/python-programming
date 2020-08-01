'''
Given a sequence of distinct non-negative integers, 
where each number is written in a separate line. The sequence 
ends with 0. Print the second largest element in this sequence. 
It is guaranteed that the sequence has at least two elements.
'''

maximum = int(input())
second_maximum = int(input())
if second_maximum > maximum:
  second_maximum, maximum = maximum, second_maximum
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    second_maximum, maximum = maximum, a
  elif a > second_maximum:
    second_maximum = a
print(second_maximum)
