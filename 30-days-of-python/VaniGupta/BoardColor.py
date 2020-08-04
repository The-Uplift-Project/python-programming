'''
Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.

The program receives two integers from 1 to 8 specifying the column and row number of the square.
'''

a = int(input())
b = int(input())

# either both x and y are even or both are odd,
# then only they'll have a black color
if (a%2 == 0 and b%2==0) or (a%2 == 1 and b%2 == 1):
  print("YES")
else:
  print("NO")
