'''
Given a string that may contain a letter p. Print the index of the second occurrence of p. 
If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.
'''

# Read a string:
s = input()
# if letter not in string
if 'p' not in s:
  print(-2)
# if only 1 occurence
elif s.count('p') == 1:
  print(-1)
else:
  i = s.index('p')
  print(s.index('p', i+1))
