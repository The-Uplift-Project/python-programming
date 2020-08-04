# Encrypt Autokey Cipher Messages

# Encrypting the message using the Autokey ciphering process
def v_encrypt(strn, k):
    st = ""
    for i in range(len(strn)):
        s = ((ord(strn[i]) + ord(k[i])) % 26) + ord('A')

        st += chr(s)
    return st


# Key function to make the key of the length of message
def key(l, st):
    t = input("Enter key : ")
    s = t
    i = 0
    while len(s) != l:
            s += st[i]
            i += 1
    return s


# Execution of the whole Encoding Process
t = ""
while t != "exit":

    print("Enter message to encrypt")
    st = input()
    k = key(len(st), st)

    e_msg = v_encrypt(st, k)
    print("Encrpted Message : "+e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
