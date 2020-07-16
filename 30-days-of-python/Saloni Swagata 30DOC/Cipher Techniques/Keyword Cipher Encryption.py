def encoder(key):
    A=[]
    for i in key:
        if i.isalpha() and i not in A:
            A.append(i)
    if len(A)>=26:
        return A
    else:
        char = 'A'
        while(len(A)!=26):
            if char not in key:
                A.append(char)
            char=chr((ord(char)+1))
        return A
            
def cipher(msg,keys):
    e = ""
    for i in msg:
        if i.isalpha():
            k = ord(i)-65
            e+=keys[k]
        else:
            e+=i
    return e


key = input("Enter the keyword: ").upper()
msg = input("Enter the message to be ciphered: ").upper()

encoded = encoder(key)
ciphermsg = cipher(msg,encoded)

print(f"Encrypted Message: {ciphermsg}")
