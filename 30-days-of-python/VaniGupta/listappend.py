# task: 
	# input: 5
	# output: [1,2,3,2,1]

	# input: 3
	# output: [1,2,1]

# user input
print("Enter an integer: ", end = "")
n = input()

# conditional checks to verify inputs
if n.isdigit() is False or int(n) < 1:
	print("Invalid input!")
	exit()

n = int(n)
l = []

# looping till mid values
for index in range(1, n//2 + 1):
	l.append(index)
if n % 2 == 1:
	l.append(n//2 + 1)

# reverse loop from mid, back to 1
for index in range(n//2, 0, -1):
	l.append(index)
	
print(l)
