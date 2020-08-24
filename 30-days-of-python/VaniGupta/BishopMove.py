'''
Chess bishop moves diagonally in any number of squares. Given two different squares of the chessboard, 
determine whether a bishop can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, 
first two - for the first square, and the last two - for the second square. The program should 
output YES if a bishop can go from the first square to the second one in a single move or NO otherwise.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# since the bishop only moves diagonally,
# difference of x and y coordinates
# should be equal

if abs(a-c) == abs(b-d):
  print("YES")
else:
  print("NO")
