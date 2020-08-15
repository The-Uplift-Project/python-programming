# Decrypt Autokey Vigenere Cipher Messages

# Decrypting the message using the Autokey Vigenere ciphering process
def va_decrypt(strn, k):
    st = ""
    for i in range(len(strn)):
        # generating the respective original message letters by comparing the encrypted message and key in the table
        s = ((ord(strn[i]) - ord(k[i]) +26) % 26) + ord('A')
        st += chr(s)
    return st

# Key function to make the key of the length of message
def key(l):
    t = input("Enter key : ")
    s = t
    i = 0
    while len(s) != l:
        # getting the key by appending the original letters after modifying it from encrypted message to original 
        s += chr(((ord(st[i]) - ord(s[i])) % 26) + ord('A'))
        i += 1
    return s

# Execution of the whole Encoding Process
t = ""
while t != "exit":

    print("Enter message to decrypt")
    st = input()
    k = key(len(st))

    e_msg = va_decrypt(st, k)
    print(e_msg)

    print("Want to decrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
