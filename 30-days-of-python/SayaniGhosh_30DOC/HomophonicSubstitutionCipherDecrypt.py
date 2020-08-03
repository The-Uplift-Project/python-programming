# Decrypt Homophonic Substitution Cipher Messages

# Decrypt function to decode and encoded msg using the given key
def hs_decrypt(strn, k):
    msg = ""
    for ch in strn:
        if ch == ' ':
            msg += ch
            continue
        for i in range(len(k)):
            lis = list(k[i])
            if ch in lis:
                msg += chars[i]


    return msg


# Key Function to interpret the given key by user
def key():
    t = list(input("Enter space seperated key for 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : "))

    li = []
    s = ""
    for i in range(len(t)):
        if t[i] == ' ':
            li.append(s)
            s = ""
            continue
        s += t[i]
        if i == len(t) - 1:
            li.append(s)
    return li


# Decoding Process of the encoded msg
t = ""
while t != "exit":
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("Enter message to decrypt")
    st = input()
    k = key()

    e_msg = hs_decrypt(st, k)
    print(e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
