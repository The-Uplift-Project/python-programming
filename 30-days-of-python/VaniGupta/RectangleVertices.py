'''
Given integer coordinates of three vertices of a rectangle whose sides are parallel to 
coordinate axes, find the coordinates of the fourth vertex of the rectangle.  
'''

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())

if x1==x3 and y2 == y3:
  print(x2)
  print(y1)
elif x2 == x3 and y1 == y2:
  print(x1)
  print(y3)
elif x1==x3 and y1==y2:
  print(x2)
  print(y3)
elif x2==x3 and y1==y3:
  print(x1)
  print(y2)
elif x1==x2 and y2==y3:
  print(x3)
  print(y1)
else:
  print(x3)
  print(y2)
