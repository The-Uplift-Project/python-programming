print("Enter the input string to be decoded: ")
text = input()
print("Enter key: ")
key = int(input())
enc_text = ""

# decryption process
for index in range(len(text)):

	# checking if element is an alphabet
	if text[index].isalpha():
		if text[index].isupper():
			temp = (ord(text[index]) - ord('A') - key)
			if temp < 0:
				temp += 26
			temp += ord('A')
			enc_text += chr(temp)

		elif text[index].islower():
			temp = (ord(text[index]) - ord('a') - key)
			if temp < 0:
				temp += 26
			temp += ord('a')
			enc_text += chr(temp)
	else:
		# if not alphabet, simply append without changes
		enc_text += text[index]

print("Old text: {0}\nDecrypted text: {1}".format(text, enc_text))
