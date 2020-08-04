def generateKey(msg, key): 
    key = list(key) 
    if len(msg) == len(key): 
        return(key) 
    else: 
        for i in range(len(msg) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

enc = input("Enter the encoded message: ")
keyword = input("Enter the keyword: ")
key = generateKey(enc, keyword)

dec_list = [] 
for i in range(len(enc)): 
    x = (ord(enc[i]) - 
         ord(key[i]) + 26) % 26
    x += ord('A') 
    dec_list.append(chr(x)) 
dec = "" . join(dec_list)

print(f"Decrypted text: {dec}")