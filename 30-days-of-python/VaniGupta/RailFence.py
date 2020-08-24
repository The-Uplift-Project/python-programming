# rail fence cipher - Only decryption

print("Enter string to be decrypted: ", end = "")
string = input()
print("Enter key for decryption (should be same as encryption): ", end = "")
key = int(input())

a = [[None for i in range(len(string))] for j in range(key)]

curr = 0
findex = 0
sindex = 0

while curr < len(string):
	if findex < key:
		while findex < key and curr < len(string):
			a[findex][sindex] = "0"
			curr += 1
			findex += 1
			sindex += 1

	if findex == key:
		findex -= 1
		while findex > 0 and curr < len(string):
			findex -= 1
			a[findex][sindex] = "0"
			curr += 1
			sindex += 1
		findex += 1

curr = 0

decrypted_string = ""

for i in a:
	for j in range(len(i)):
		if i[j] == "0":
			i[j] = string[curr]
			curr += 1

curr = 0
findex = 0
sindex = 0

while curr < len(string):
	if findex < key:
		while findex < key and curr < len(string):
			decrypted_string += a[findex][sindex]
			curr += 1
			findex += 1
			sindex += 1

	if findex == key:
		findex -= 1
		while findex > 0 and curr < len(string):
			findex -= 1
			decrypted_string += a[findex][sindex]
			curr += 1
			sindex += 1
		findex += 1

print("Decrypted string:",decrypted_string)
