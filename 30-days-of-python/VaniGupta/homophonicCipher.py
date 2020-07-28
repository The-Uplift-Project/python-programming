key_table = {
'A':['21','27','31','40'],
'B':['15'],
'C':['01','33'],
'D':['20','34'],
'E':['22','28','32','36','37'],
'F':['05'],
'G':['17'],
'H':['14'],
'I':['02','29','38','41'],
'J':['19'],
'K':['03'],
'L':['07','39','42'],
'M':['09','43'],
'N':['12','48','97'],
'O':['18','60','85'],
'P':['26','44'],
'Q':['25'],
'R':['24','49'],
'S':['10','30','45','99'],
'T':['06','96','55'],
'U':['16','94'],
'V':['23'],
'W':['13'],
'X':['11'],
'Y':['08'],
'Z':['04']
}

import random
s = input()
def encrypt(s):
    st = ""
    for item in s:
        if item.upper() in key_table:
            st += random.choice(key_table[item.upper()])
        else:
            st += item
    return st

def decrypt(s):
    words = s.split()
    lst = []
    for item in words:
        for i in range(0,len(item), 2):
            lst.append(item[i:i+2])
        lst.append(" ")
    res = ""
    for char in lst:
        if char == " ":
            res += " "
        for item in key_table:
            if char in key_table[item]:
                res += item.lower()
    return res

enc = encrypt(s)
dec = decrypt(enc)
print("Encryption of message:{} => {}".format(s, enc))
print("Decryption of message:{} => {}".format(enc, dec))
