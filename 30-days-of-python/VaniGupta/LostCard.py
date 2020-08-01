'''
There was a set of cards with numbers from 1 to N. 
One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.

Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct 
integers in the range from 1 to N). Find and print the number on the lost card.
'''

# Read an integer:
a = int(input())

# create another list from numbers 1 to a-1
b = [int(input()) for _ in range(a-1)]

for i in range(1,a+1):
  if i not in b:
    print(i)
    break
    
# another way could be used by using sort()
