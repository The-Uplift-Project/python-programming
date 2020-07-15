s = input("Enter the string to be encrypted: ")
e=""
for letter in s:
    if letter.isupper():
         e+= chr((ord(letter) + 3-65) % 26 + 65)
    else:
        e += chr((ord(letter) + 3 - 97) % 26 + 97)
print(f"Encryted String: {e}")
