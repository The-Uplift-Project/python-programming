s = input("Enter the string to be decrypted: ")
d=""
for letter in s:
    if letter.isupper():
         d+= chr((ord(letter) + 23-65) % 26 + 65)
    else:
        d+= chr((ord(letter) + 23 - 97) % 26 + 97)
print(f"Decryted String: {d}")
