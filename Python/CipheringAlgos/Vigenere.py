chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def Enc(txt, k):

    # transforming key to length of message
    ls = ""
    i = 0
    while len(ls) != len(txt):
        ls += k[i]
        if i == len(k) - 1:
            i = 0
            continue
        i += 1

    # Encrypting the message
    if txt.isupper():
        st = ""
        for i in range(len(txt)):
            if txt[i] not in chars:
                st += txt[i]
                continue
            s = ((ord(txt[i]) + ord(ls[i])) % 26) + ord('A')
            st += chr(s)

        return st
    if txt.islower():
        txt = txt.upper()
        ls = ls.upper()
        st = ""
        for i in range(len(txt)):
            if txt[i] not in chars:
                st += txt[i]
                continue
            s = ((ord(txt[i]) + ord(ls[i])) % 26) + ord('a')
            st += chr(s)
        st = st.lower()

        return st

def Dec(txt, k):
    # transforming key to length of message
    ls = ""
    i = 0
    while len(ls) != len(txt):
        ls += k[i]
        if i == len(k) - 1:
            i = 0
            continue
        i += 1

    # Decrypting the message
    if txt.isupper():
        st = ""
        for i in range(len(txt)):
            if txt[i] not in chars:
                st += txt[i]
                continue
            s = ((ord(txt[i]) - ord(ls[i]) + 26) % 26) + ord('A')
            st += chr(s)

        return st
    if txt.islower():
        txt = txt.upper()
        ls = ls.upper()
        st = ""
        for i in range(len(txt)):
            if txt[i] not in chars:
                st += txt[i]
                continue
            s = ((ord(txt[i]) - ord(ls[i]) + 26) % 26) + ord('a')
            st += chr(s)
        st = st.lower()

        return st
