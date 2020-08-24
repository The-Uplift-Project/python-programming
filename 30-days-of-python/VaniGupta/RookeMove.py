'''
Chess rook moves horizontally or vertically. Given two different squares of the chessboard, 
determine whether a rook can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - 
for the first square, and the last two - for the second square. The program should output YES 
if a rook can go from the first square to the second one in a single move or NO otherwise
'''

# Read an integer:
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# since the rook can only move in vertical or 
# horizontal direction, either both
# x or y coordinates should be equal
if (a == c and b != d) or (a != c and b == d):
  print("YES")
else:
  print("NO")
