import random
# Encrypt Homophobic Substitution Cipher Messages


def hs_encrypt(strn, k):
    msg = ""
    for ch in strn:
        if ch in chars:
            lis = list(k[chars.find(ch)])
            msg += random.choice(lis)
    return msg

def key():
    t = list(input("Enter space seperated key for ' ' ',' '.' and 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : "))

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

t = ""
while t != "exit":
    chars = " ,.ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("Enter message to encrypt")
    st = input()
    k = key()

    e_msg = hs_encrypt(st, k)
    print(e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
