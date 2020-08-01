'''
Write a program that solves a linear equation ax = b in integers. 
Given two integers a and b (a may be zero), print a single integer 
root if it exists and print "no solution" or "many solutions" otherwise.
'''

a = int(input())
b = int(input())

if a==0 and b==0:
  print("many solutions")
elif a == 0 and b!=0:
    print("no solution") 
else:
  if int(b/a) * a == b:
    print(int(b/a))
  else:
    print("no solution")
