# rail fence cipher
# level hard

print("Enter string to be encrypted: ", end = "")
string = input()
print("Enter key for encryption (works best for small key values) : ", end = "")
key = int(input())

while key >= len(string):
	print("Please enter a smaller value: ", end = "")
	key = int(input())

a = [[None for i in range(len(string))] for j in range(key)]

curr = 0
findex = 0
sindex = 0

while curr < len(string):
	if findex < key:
		while findex < key and curr < len(string):
			a[findex][sindex] = string[curr]
			curr += 1
			findex += 1
			sindex += 1
