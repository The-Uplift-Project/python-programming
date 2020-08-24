'''
Chess knight can move to a square that is two squares away horizontally and one square vertically, 
or two squares vertically and one square horizontally. 
The complete move therefore looks like the letter L. Given two different squares of the chessboard, 
determine whether a knight can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, 
first two - for the first square, and the last two - for the second square. 
The program should output YES if a knight can go from the first square to the second one in a single move or NO otherwise.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 2 moves forward and 1 move in either left or right direction,
# or, 1 move forward and 2 moves in either right ir left direction

if abs(a-c) == 2 and abs(b-d) == 1 or abs(b-d) == 2 and abs(a-c) == 1:
  print("YES")
else:
  print("NO")
