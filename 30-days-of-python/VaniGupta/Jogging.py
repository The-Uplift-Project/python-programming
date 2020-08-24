'''
As a future athlete you just started your practice for an upcoming event. 
On the first day you run x miles, and by the day of the event you must be able to run y miles.

Calculate the number of days required for you to finally reach the required distance for 
the event, if you increases your distance each day by 10% from the previous day.

Print one integer representing the number of days to reach the required distance.
'''
# Read an integer:
x = int(input())
y = int(input())
# counter
c = 0
while x < y:
  x += (x / 10)
  c += 1
print(c + 1)
