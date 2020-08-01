def generateKey(msg, key): 
    key = list(key) 
    if len(msg) == len(key): 
        return(key) 
    else: 
        for i in range(len(msg) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

msg = input("Enter the message to be encrypted: ")
keyword = input("Enter the Keyword: ")
key = generateKey(msg, keyword) 
enc_list = [] 
for i in range(len(msg)): 
    x = (ord(msg[i]) + 
         ord(key[i])) % 26
    x += ord('A') 
    enc_list.append(chr(x)) 
enc="" . join(enc_list)

print(f"Encrypted message: {enc}")