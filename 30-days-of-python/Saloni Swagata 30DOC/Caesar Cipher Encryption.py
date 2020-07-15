s = input("Enter the string to be encrypted: ").split()
d=""
if len(s)>1:
    for word in s:
        word.upper()
        for letter in word:
            k = ord(letter)-65
            n = (k+3)%26
            d+=chr(n)
        d+=" "
else:
    S=s[0]
    S.upper()
    for letter in S:
        k = ord(letter)-65
        n = (k+3)%26
        d+=chr(n)
print(f"Encryted String: {d}")
