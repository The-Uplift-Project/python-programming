# Decrypt Autokey Cipher Messages

# Decrypting the message using the Autokey ciphering process
def v_encrypt(strn, k):
    st = ""
    for i in range(len(strn)):
        s = ((ord(strn[i]) - ord(k[i])) % 26) + ord('A')

        st += chr(s)
    return st


# Key function to make the key of the length of message
def key(l, st):
    t = input("Enter key : ")
    s = t
    i = 0
    while len(s) != l:
            s += chr(((ord(st[i]) - ord(s[i])) % 26) + ord('A'))
            i += 1
    return s


# Execution of the whole Decoding Process
t = ""
while t != "exit":

    print("Enter message to decrypt")
    st = input()
    k = key(len(st), st)
    e_msg = v_encrypt(st, k)
    print("Original message : "+e_msg)

    print("Want to decrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
