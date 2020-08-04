import random

key_table={'A':['D','9'],'B':'X','C':'S','D':'F','E':['Z','7','2','1'],'F':'E','G':'H','H':'C','I':['V','3'],'J':'I','K':'T','L':'P','M':'G','N':['A','5'],'O':['Q','0'],'P':'L','Q':'K','R':'J','S':['R','4'],'T':['U','6'],'U':'O','V':'W','W':'M','X':'Y','Y':'B','Z':'N'}

msg = input("Enter the message to be encrypted: ").upper()

enc=""

for i in msg:
    if i in key_table:
        if isinstance(key_table[i], list):
            enc+=random.choice(key_table[i])
        else:
            enc+=key_table[i]
    else:
        enc+=i

print(f"Encrypted message: {enc}")
