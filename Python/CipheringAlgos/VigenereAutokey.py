chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Enc(strn, key):

    # Encrypting process
    if strn.isupper():
        # Creating key upto message length
        i = 0
        while len(key) != len(strn):
            key += strn[i]
            i += 1
        # encryption
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) + ord(key[i])) % 26) + ord('A')
            st += chr(s)
        return st

    if strn.islower():
        strn = strn.upper()
        key = key.upper()
        # Creating key upto message length
        i = 0
        while len(key) != len(strn):
            key += strn[i]
            i += 1
        # encryption
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) + ord(key[i])) % 26) + ord('A')
            st += chr(s)
        st = st.lower()

        return st



def Dec(strn, key):
    # Decryption process
    if strn.isupper():
        # Creating key
        i = 0
        while len(key) != len(strn):
            key += chr(((ord(strn[i]) - ord(key[i])) % 26) + ord('A'))
            i += 1
        # decryption
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) - ord(key[i]) + 26) % 26) + ord('A')
            st += chr(s)
        return st

    if strn.islower():
        strn = strn.upper()
        key = key.upper()
        # Creating key
        i = 0
        while len(key) != len(strn):
            key += chr(((ord(strn[i]) - ord(key[i])) % 26) + ord('A'))
            i += 1
        # decryption
        st = ""
        for i in range(len(strn)):
            if strn[i] not in chars:
                st += strn[i]
                continue
            s = ((ord(strn[i]) - ord(key[i]) + 26) % 26) + ord('A')
            st += chr(s)
        st = st.lower()
        return st
