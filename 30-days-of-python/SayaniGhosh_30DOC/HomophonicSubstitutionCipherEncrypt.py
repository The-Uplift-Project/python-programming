import random
# Encrypt Homophonic Substitution Cipher Messages

# Encrypt function to return the encoded message using key given by users
def hs_encrypt(strn, k):
    msg = ""
    for ch in strn:
        if ch in chars:
            lis = list(k[chars.find(ch)])
            msg += random.choice(lis)
        else:
            msg += ch
    return msg

# key function to return key value for each letter according to users to increase security
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

# Execution of the Encoding Process
t = ""
while t != "exit":
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("Enter message to encrypt")
    st = input()
    k = key()

    e_msg = hs_encrypt(st, k)
    print(e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
