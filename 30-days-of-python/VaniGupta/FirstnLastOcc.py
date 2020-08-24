'''
Given a string that may contain a letter f. 
Print the index of the first and last occurrence of f. 
If the letter f occurs only once, then output its index once. 
If the letter f does not occur, print -1.
'''

# Read a string:
s = input()
# if letter not present in string input
if 'f' not in s:
  print(-1)
else:
  # if only one occurence
  if s.count('f') == 1:
    print(s.index('f'))
  else:
    print(s.index('f'), len(s) - s[::-1].index('f') - 1)

