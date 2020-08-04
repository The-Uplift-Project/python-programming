'''
Given a list of non-zero integers, find and print the first 
adjacent pair of elements that have the same sign. 
If there is no such pair, print 0.
'''

# Read a list of integers:
a = [int(s) for s in input().split()]
# Print a value:
# print(a)
flag = 0
for i in range(len(a) - 1):
  if a[i] < 0 and a[i+1] < 0 or a[i] > 0 and a[i+1] > 0:
    flag = 1
    print(a[i], a[i+1])
    break
if flag == 0:
  print(0)
# another way could be by multiplying and checking sign
