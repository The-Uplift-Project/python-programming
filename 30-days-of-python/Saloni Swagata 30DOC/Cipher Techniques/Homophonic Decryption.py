key_table={'A':['D','9'],'B':'X','C':'S','D':'F','E':['Z','7','2','1'],'F':'E','G':'H','H':'C','I':['V','3'],'J':'I','K':'T','L':'P','M':'G','N':['A','5'],'O':['Q','0'],'P':'L','Q':'K','R':'J','S':['R','4'],'T':['U','6'],'U':'O','V':'W','W':'M','X':'Y','Y':'B','Z':'N'}

enc = input("Enter the encoded message: ").upper()

dec=""
for i in enc:
    if i.isalnum():
        k=0
        for j in key_table.values():
            if i in j:
                break
            k+=1
        dec+=chr(65+k)
    else:
        dec+=i

print(f"Decrypted message: {dec}")